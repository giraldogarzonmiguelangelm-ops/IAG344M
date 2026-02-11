function downloadPDF(){
    const element = document.querySelector("#pdf-content")
    //console.log(element);
    const otp = {
        margin: [20, 5, 55, 5], //[arriba10, izquierda5, abajo15, derecha5] en mm
        filename: 'Hoja_de_vida_Miguel_Giraldo.pdf',
        image: { type: 'jpeg', quality: 1 },
        html2canvas:{
            scale: 2,
            useCORS: true,
            scrollY: 0,

        },
        jsPDF:{
            unit: 'mm',
            format: 'a4',
            orientation: 'portrait' //Orientación Vertical
        }
    }
    html2pdf().set(otp).from(element).save();

}