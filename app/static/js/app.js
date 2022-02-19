/* Add your Application JavaScript */
window.addEventListener('load', (event)=>{

    setInterval( ()=>{
        let flashcontainer= document.querySelector("#flashmsg");
        if (document.contains(flashcontainer)){
            flashcontainer.innerHTML="";
            flashcontainer.classList.remove("pass");
        }
    }, 3000)
});