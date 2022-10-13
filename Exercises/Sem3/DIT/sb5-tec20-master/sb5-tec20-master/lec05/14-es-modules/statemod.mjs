let innerState = undefined;
export function setState(newState) { innerState = newState; }
export function getState() { return innerState; }

export default {setState, getState}