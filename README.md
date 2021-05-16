# msd.js
/* Codded by @phaticusthiccy
Telegram: t.me/phaticusthiccy
Instagram: www.instagram.com/kyrie.baran
*/
const Asena = require('../events');
const{MessageType} = require('@adiwajshing/baileys');

Asena.addCommand({pattern: 'msd', fromMe: true}, (async (message, match) => {

await message.sendMessage('Bu bir testtir!');
await new Promise(r => setTimeout(r, 1000));

await message.sendMessage('Test Bitti!');

}));

    }

}

// Plugin End
