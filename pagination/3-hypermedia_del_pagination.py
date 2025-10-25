#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination module.

This extends the pagination system to handle dataset deletions
without breaking pagination consistency.
"""

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index
                         for the items corresponding to the given page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """
    Server class to paginate a database of popular baby names,
    supporting deletion-resilient pagination.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with an empty dataset cache."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache dataset from CSV file.

        Returns:
            List[List]: The dataset loaded from the CSV file,
                        with the header row removed.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding='utf-8') as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Create an indexed dataset.

        Returns:
            Dict[int, List]: A dictionary mapping index
            positions to dataset rows.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range
                                      (len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict[str, Any]:
        """
        Retrieve a page of the dataset with a deletion-resilient index.

        Args:
            index (int, optional): The current start index of the return page.
                                   Defaults to None.
            page_size (int, optional): The number of items per page.
                                       Defaults to 10.

        Returns:
            Dict[str, Any]: A dictionary containing:
                - index: current start index
                - next_index: index to query next
                - page_size: current page size
                - data: the dataset page

        Raises:
            AssertionError: If index is out of valid range or negative.
        """
        indexed_data = self.indexed_dataset()
        dataset_size = len(indexed_data)

        if index is None:
            index = 0

        assert isinstance(index, int) and 0 <= index < dataset_size, \
            "index must be a valid integer within dataset range"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        data: List[List] = []
        current_index = index

        # Collect the data for the page_size, skipping deleted indices
        while len(data) < page_size and current_index < dataset_size:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        next_index = current_index if current_index < dataset_size else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
