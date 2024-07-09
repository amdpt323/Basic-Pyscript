from pyscript import document

def submit_form(event):
    event.preventDefault()
    string1 = document.querySelector("#string1")
    string2 = document.querySelector("#string2")
    string3 = document.querySelector("#string3")
    output_div = document.querySelector("#output")
    output_div.innerText = f"You entered: {string1.value} , {string2.value}  , {string3.value}"
    string1.value=""
    string2.value=""
    string3.value=""
 
