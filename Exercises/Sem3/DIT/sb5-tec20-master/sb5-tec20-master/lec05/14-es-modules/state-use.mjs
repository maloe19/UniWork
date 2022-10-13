import statemod from './statemod.mjs';

console.log(statemod.getState());
statemod.setState(1);
console.log(statemod.getState());
statemod.setState(2);
console.log(statemod.getState());