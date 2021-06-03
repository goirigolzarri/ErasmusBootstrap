const { nodeName } = require("jquery");

function recogeID(clickID){ 

    document.getElementById("id_studentType").value = clickID;
   

    if (clickID == 1) {
        // NOT Displayed   
        document.getElementById("companyDiv").style.display = "none";
        // NOT Required
        if( document.getElementById('id_company').value != null ){
            document.getElementById('id_company').value= '' ;
        }
        document.getElementById("id_company").removeAttribute("required");
        
        // DISPLAYED
        document.getElementById("studiesDiv").style.display = "";
        // REQUIRED
        document.getElementById("id_studies").setAttribute("required", "");
        // DISPLAYED
        document.getElementById("courseDiv").style.display = "";
        // REQUIRED
        document.getElementById("id_course").setAttribute("required", "");
        // DISPLAYED
        document.getElementById("universityOriginDiv").style.display = "";
        // REQUIRED
        document.getElementById("id_universityOrigin").setAttribute("required", "");
        // DISPLAYED
        document.getElementById("universityDestinationDiv").style.display = "";
        // REQUIRED
        document.getElementById("id_universityDestination").setAttribute("required", "");

    }
    if (clickID == 2) {
        document.getElementById("companyDiv").style.display = "none";
        // NOT Required
        if( document.getElementById('id_company').value != null ){
            document.getElementById('id_company').value= '' ;
        }
        document.getElementById("id_company").removeAttribute("required");
        
        // NOT Displayed   
        document.getElementById("studiesDiv").style.display = "none";  
        // NOT Required
        if( document.getElementById('id_studies').value != null ){
            document.getElementById('id_studies').value= '' ;
        }
        document.getElementById("id_studies").removeAttribute("required");
        
        // NOT Displayed   
        document.getElementById("courseDiv").style.display = "none";
        // NOT Required
        if( document.getElementById('id_course').value != null ){
            document.getElementById('id_course').value= '' ;
        }
        document.getElementById("id_course").removeAttribute("required");
        
        // NOT Displayed   
        document.getElementById("universityOriginDiv").style.display = "none";
        // NOT Required
        if( document.getElementById('id_universityOrigin').value != null ){
            document.getElementById('id_universityOrigin').value= '' ;
        }
        document.getElementById("id_universityOrigin").removeAttribute("required");
        
        
        // NOT Displayed   
        document.getElementById("universityDestinationDiv").style.display = "none";
        // NOT Required
        if( document.getElementById('id_universityDestination').value != null ){
            document.getElementById('id_universityDestination').value= '' ;
        }
        document.getElementById("id_universityDestination").removeAttribute("required");
        
    }
    if (clickID == 3) {
        // NOT Displayed   
        document.getElementById("companyDiv").style.display = "none";
        // NOT Required
        if( document.getElementById('id_company').value != null ){
            document.getElementById('id_company').value= '' ;
        }
        document.getElementById("id_company").removeAttribute("required");
        
        // NOT Displayed   
        document.getElementById("courseDiv").style.display = "none";
        // NOT Required
        if( document.getElementById('id_course').value != null ){
            document.getElementById('id_course').value= '' ;
        }
        document.getElementById("id_course").removeAttribute("required");
        
        // DISPLAYED
        document.getElementById("studiesDiv").style.display = "";
        // REQUIRED
        document.getElementById("id_studies").setAttribute("required", "");
        // DISPLAYED
        document.getElementById("universityOriginDiv").style.display = "";
        // REQUIRED
        document.getElementById("id_universityOrigin").setAttribute("required", "");
        // DISPLAYED
        document.getElementById("universityDestinationDiv").style.display = "";
        // REQUIRED
        document.getElementById("id_universityDestination").setAttribute("required", "");
    }
    if (clickID == 4) {
        document.getElementById("companyDiv").style.display = "";
        // REQUIRED
        document.getElementById("id_company").setAttribute("required", "");

        // NOT Displayed  
        document.getElementById("courseDiv").style.display = "none";
        // NOT Required
        if( document.getElementById('id_course').value != null ){
            document.getElementById('id_course').value= '' ;
        }
        document.getElementById("id_course").removeAttribute("required");
        
        // NOT Displayed  
        document.getElementById("studiesDiv").style.display = "none";
        // NOT Required
        if( document.getElementById('id_studies').value != null ){
            document.getElementById('id_studies').value= '' ;
        }
        document.getElementById("id_studies").removeAttribute("required");
        
        // NOT Displayed  
        document.getElementById("universityOriginDiv").style.display = "none";
        // NOT Required
        if( document.getElementById('id_universityOrigin').value != null ){
            document.getElementById('id_universityOrigin').value= '' ;
        }
        document.getElementById("id_universityOrigin").removeAttribute("required");
        
        // NOT Displayed  
        document.getElementById("universityDestinationDiv").style.display = "none";
        // NOT Required
        if( document.getElementById('id_universityDestination').value != null ){
            document.getElementById('id_universityDestination').value= '' ;
        }
        document.getElementById("id_universityDestination").removeAttribute("required");
        
    }
}

function showHide(checked) {
    
    //check = document.getElementById("box1");
    if (checked == true) {
        //document.getElementById("cityDestination2Div").style.display ='block';
        $("#cityDestination2Div").fadeIn();
        $("#cityDestination3Div").fadeIn();
    } 
    else{
        $("#cityDestination2Div").fadeOut();
        $("#cityDestination3Div").fadeOut();
    }   
}



// window.onload = function() {
//     document.getElementById("id_studentType").onchange = Hide;
// };




    // alert(clickID);
   

