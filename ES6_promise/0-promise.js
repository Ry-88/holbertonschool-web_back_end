export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    // Simulate an asynchronous operation, e.g., API call
    setTimeout(() => {
      const success = true; // or false to simulate error
      if (success) {
        resolve('Response received');
      } else {
        reject(new Error('API Error'));
      }
    }, 1000); // 1 second delay
  });
}
