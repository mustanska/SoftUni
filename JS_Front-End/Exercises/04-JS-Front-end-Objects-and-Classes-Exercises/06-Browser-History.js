function solve(inputObject, inputArray) {
    for (const action of inputArray) {
        let [move, site] = action.split(' ');

        if(move === 'Open'){
            openTab(inputObject, action, site);
        } else if(move === 'Close'){
            closeTab(inputObject, action, site);
        }else {
            clearHistoryAndCache(inputObject);
        }
    }
    
    printResult(inputObject);

    function openTab(object, action, site) {
        object['Open Tabs'].push(site);
        object['Browser Logs'].push(action);
    }

    function closeTab(object, action, site) {
        let sitePosition = object['Open Tabs'].indexOf(site);

        if(sitePosition !== -1) {
            object['Open Tabs'].splice(sitePosition, 1);
            object['Recently Closed'].push(site);
            object['Browser Logs'].push(action);
        }
    }

    function clearHistoryAndCache(object) {
        object['Open Tabs'] = [];
        object['Recently Closed'] = [];
        object['Browser Logs'] = [];
    }

    function printResult(object) {
        console.log(object['Browser Name']);
        console.log(`Open Tabs: ${object['Open Tabs'].join(', ')}`);
        console.log(`Recently Closed: ${object['Recently Closed'].join(', ')}`);
        console.log(`Browser Logs: ${object['Browser Logs'].join(', ')}`);
    }
}

solve(
    {"Browser Name":"Google Chrome","Open Tabs":["Facebook","YouTube","Google Translate"],
    "Recently Closed":["Yahoo","Gmail"],
    "Browser Logs":["Open YouTube","Open Yahoo","Open Google Translate","Close Yahoo","Open Gmail","Close Gmail","Open Facebook"]},
    ["Close Facebook", "Open StackOverFlow", "Open Google"]
);
solve(
    {"Browser Name":"Mozilla Firefox",
    "Open Tabs":["YouTube"],
    "Recently Closed":["Gmail", "Dropbox"],
    "Browser Logs":["Open Gmail", "Close Gmail", "Open Dropbox", "Open YouTube", "Close Dropbox"]},
    ["Open Wikipedia", "Clear History and Cache", "Open Twitter"]
);