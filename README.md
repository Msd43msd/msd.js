const Asena = require('../events');
const{MessageType} = require('@adiwajshing/baileys');

Asena.addCommand({pattern: 'msd', fromMe: true, onlyPm: false}, (async (message, match) => {

if (match[1] === "bir") {
    awaitmessage.sendMessage('test bir yazarsınız bu mesajı verir');


} else if (match[1] === "iki") {
    awaitmessage.sendMessage('test iki yazarsınız bu mesajı verir');


} else {
    await message.sendMessage('Yukardaki parametreler girilmezse bu mesaj gelecektir');
}


}));
