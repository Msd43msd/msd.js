const Asena = require('../events');
const{MessageType} = require('@adiwajshing/baileys');

Asena.addCommand({pattern: 'msd', fromMe: true, onlyPm: false}, (async (message, match) => {

await message.sendMessage('Bu bir testtir!');
await new Promise(r => setTimeout(r, 1000));


}));
