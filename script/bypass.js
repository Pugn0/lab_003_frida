Java.perform(function () {
    const MobileExploitationData = Java.use('br.com.mobileexploitation.a003variables.MobileExploitationData');

    MobileExploitationData.setData.implementation = function () {
        const resultado = this.setData();
        console.log('Método setData() interceptado - mTextData1:', this.mTextData1.value);
        console.log('Método setData() interceptado - mTextData2:', this.mTextData2.value);
        return resultado;
    };

    MobileExploitationData.setData3.overload('java.lang.String').implementation = function (str) {
        this.setData3(str);
        console.log('Método setData3(String) interceptado - mTextData3:', this.mTextData3.value);
    };
});