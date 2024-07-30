const usernameField=document.querySelector("#usernameField")
const emailField=document.querySelector("#emailField")
const showpasswordField=document.querySelector(".show-password")
const passwordField=document.querySelector("#passwordField")
const submitBtn=document.querySelector('.submit-btn')
const messageField=document.querySelector(".messages")

const handleToggleInput=(e)=>{
    if(showpasswordField.textContent==="SHOW"){
        showpasswordField.textContent="HIDE"
        passwordField.setAttribute("type","text");
    }
    else{
        showpasswordField.textContent="SHOW"
        passwordField.setAttribute("type","password");
    }
}

showpasswordField.addEventListener("click",handleToggleInput);

usernameField.addEventListener("keyup",(e)=>{
    const usernameVal=e.target.value;
    usernameField.classList.remove("is-invalid")
    if(usernameVal.length > 0){
        fetch("/authentication/validate-username",{
            body:JSON.stringify({
                username:usernameVal
            }),
            method:"POST",
        }).then(res=>res.json()).then(data=>{
            console.log("data",data);
            if(data.username_error){
                usernameField.classList.add("is-invalid");
                submitBtn.setAttribute('disabled','true');
            }
            else{
                submitBtn.removeAttribute('disabled');
            }
        });
    }

});

emailField.addEventListener("keyup",(e)=>{
    const emailVal=e.target.value;
    emailField.classList.remove("is-invalid")
    if(emailVal.length > 0){
        fetch("/authentication/validate-email",{
            body:JSON.stringify({
                email:emailVal
            }),
            method:"POST",
        }).then(res=>res.json()).then(data=>{
            console.log("data",data);
            if(data.email_error){
                emailField.classList.add("is-invalid");
                submitBtn.setAttribute('disabled','true');
            }
            else{
                submitBtn.removeAttribute('disabled');
            }
        });
    }

});

window.addEventListener('load',()=>{
    if(messageField){
        messageField.innerHTML='';
    }
})
