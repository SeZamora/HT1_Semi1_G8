const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.sendStatus(200);
});
app.get('/check', (req, res) => {
    res.sendStatus(200);
});

app.get('/info', (req, res) => {
    res.json({
        Instancia: "Maquina 2 - API 2",
        Curso: "Seminario de Sistemas 1 A",
        Grupo : "Grupo 8"
    });
});

const PORT = 5000;
app.listen(PORT, () => {
    console.log(`API corriendo en http://0.0.0.0:${PORT}`);
});
