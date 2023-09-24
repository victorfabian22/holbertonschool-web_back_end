import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const x = new Array(3);// Array de objetos que retornaremos
  const numbers = [19, 20, 34];// Numeros a pasar a la clase 'ClassRoom'

  for (const i in numbers) { // Iteramos en los números
    if (Object.prototype.hasOwnProperty.call(numbers, i)) {
      const newObject = new ClassRoom(numbers[i]);
      x[i] = newObject;
    }
  }
  return x;
}
