const tar = document.querySelector("#\\32 387440830 > div > div > div.rax-view-v2.tmg-marketing-coupon-content-right > div");
// const tar2 = document.querySelector("#\\34 272539560 > div > div > div.rax-view-v2.tmg-marketing-coupon-content-right > div");
const a = new Date();
const TARGET_EPOCH_TIME = new Date(a.getFullYear(), a.getMonth(), a.getDate() , 19,59,59,800).getTime();
const nowTime = new Date();
console.log("Now Time:" + nowTime.toLocaleString());
console.log("Wait Time:" + (TARGET_EPOCH_TIME - nowTime.getTime())/1000.0 + " seconds");
const  currentEpochTime = new Date();

function c(){
    tar.click();
}
// function c2(){
//     tar2.click();
// }

function executeattime(){
    const currentEpochTime = new Date();
    if (TARGET_EPOCH_TIME - currentEpochTime.getTime() > 60000 ) {
        console.log("Current Epoch Time:" + currentEpochTime.toLocaleString());
        setTimeout(executeattime, 25000);
    }
    else if (TARGET_EPOCH_TIME > currentEpochTime.getTime()) {
        console.log("Current Epoch Time:" + currentEpochTime.toLocaleString());
        setTimeout(executeattime, 200);
    } else {
        c();
        // setTimeout(c2,150);
        setTimeout(c,150);
        // setTimeout(c2,150);
        setTimeout(c,250);
        setTimeout(c,349);
        // tar.click();
        // tar.click();
    }
}

executeattime();



