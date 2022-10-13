let innerState = undefined;
exports.setState = newState => { innerState = newState; }
exports.getState = () => { return innerState; }

//exports default {setState, getState}