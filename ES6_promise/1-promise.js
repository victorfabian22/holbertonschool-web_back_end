export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      resolve({ status: 200, body: 'Success' });
    } else {
      const msg = new Error('The fake API is not working currently');
      reject(msg);
    }
  });
}
