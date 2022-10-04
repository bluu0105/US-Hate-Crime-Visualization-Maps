
const containerDiv1 = document.getElementById('vizContainer1');
const url1 = 'https://public.tableau.com/views/EthnicityRaceMotivated/EthnicityRaceMap?:language=en-US&:display_count=n&:origin=viz_share_link';
const options1 = {
    hideTabs: true,
    hideToolbar: true,
    height: 1000,
    width: 1000
}

const containerDiv2 = document.getElementById('vizContainer2');
const url2 = 'https://public.tableau.com/views/ReligionMotivated/ReligionMap?:language=en-US&:display_count=n&:origin=viz_share_link';
const options2 = {
    hideTabs: true,
    hideToolbar: true,
    height: 1000,
    width: 1000
}

const containerDiv3 = document.getElementById('vizContainer3');
const url3 = 'https://public.tableau.com/views/SexualOrientationMotivated/SexualOrientationMap?:language=en-US&:display_count=n&:origin=viz_share_link';
const options3 = {
    hideTabs: true,
    hideToolbar: true,
    height: 1000,
    width: 1000
}

function initViz() {
    let viz1 = new tableau.Viz(containerDiv1, url1, options1);
    let viz2 = new tableau.Viz(containerDiv2, url2, options2);
    let viz3 = new tableau.Viz(containerDiv3, url3, options3);
}