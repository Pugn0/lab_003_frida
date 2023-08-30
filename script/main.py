import frida

# Nome do pacote do aplicativo alvo
nome_pacote = 'br.com.mobileexploitation.a003variables'

# Script Frida para interceptar métodos da classe
script_frida = """
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
"""

# Função para lidar com mensagens recebidas do script Frida
def on_message(message, data):
    print("[*] Mensagem recebida:", message)

# Conectar-se ao dispositivo USB
device = frida.get_usb_device()

# Obter o processo do aplicativo alvo
processo = device.attach(nome_pacote)

# Criar uma sessão Frida
sessao = processo.create_script(script_frida)
sessao.on('message', on_message)

# Injetar o script no processo e iniciar
sessao.load()

# Manter o script em execução
try:
    print("Pressione Ctrl+C para encerrar.")
    frida.get_event_loop().run_forever()
except KeyboardInterrupt:
    pass
