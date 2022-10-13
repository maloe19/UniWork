const state = (function () {
    let innerState = undefined;
    function setState(newState) { innerState = newState; }
    function getState() { return innerState; }
    return {setState, getState};
})();
