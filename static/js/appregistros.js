/*
 * A Design by GMSoftSolutions
 * Authors: George Navarro & Maria Caridad Pons
 * License: GM SoftSolutions
 */

jQuery(document).ready(function ($) {

/* Send Email cuando se registra un usuario interesado en un seminario */
    $("#send-mail-registro").click(function () {
        var name = $('#namereg').val(); // get the value of the input field
        var error = false;
        if (name == "" || name == " ") {
            $('#err-namereg').show(500);
            $('#err-namereg').delay(4000);
            $('#err-namereg').animate({
                height: 'toggle'
            }, 500, function () {
                // Animation complete.
            });
            error = true; // change the error state to true
        }

        var emailCompare = /^([a-z0-9_.-]+)@([da-z.-]+).([a-z.]{2,6})$/; // Syntax to compare against input
        var email = $('#emailreg').val().toLowerCase(); // get the value of the input field
        if (email == "" || email == " " || !emailCompare.test(email)) {
            $('#err-emailreg').show(500);
            $('#err-emailreg').delay(4000);
            $('#err-emailreg').animate({
                height: 'toggle'
            }, 500, function () {
                // Animation complete.
            });
            error = true; // change the error state to true
        }

        var comment = $('#commentreg').val(); // get the value of the input field
//        if (comment == "" || comment == " ") {
//            $('#err-comment').show(500);
//            $('#err-comment').delay(4000);
//            $('#err-comment').animate({
//                height: 'toggle'
//            }, 500, function () {
//                // Animation complete.
//            });
//            error = true; // change the error state to true
//        }

        if (error == false) {
            var crmw = document.getElementsByName("csrfmiddlewaretoken")[0].value;
            var materiaid = $("#materiaid").val();
//            $.blockUI({"message": null});
            $.post("/registrointeres", {"nombre": name, "email": email, "mensaje": comment, "materiaid": materiaid, "csrfmiddlewaretoken":crmw}, function(data){
//                $.unblockUI();
                if (data.result=='ok'){
                    $("#namereg").val('');
                    $("#emailreg").val('');
                    $("#commentreg").val('');

                    //Mostrar mensaje de exito de envio hy luego esconder a los 3 seg
                    $('#successSendReg').show();
                    setTimeout(function() {
                        $('#successSendReg').fadeOut("slow");
                    }, 3000);

                }else{
                    //Mostrar mensaje de fallo en envio
                    $('#errorSendReg').show();
                    setTimeout(function() {
                        $('#errorSendReg').fadeOut("slow");
                    }, 3000);

                }

            }, "json");

        }

        return false;
    });

});