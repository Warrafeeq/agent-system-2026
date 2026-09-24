const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.json());

app.get('/api/health', (req, res) => {
  res.json({ status: 'healthy' });
});

app.get('/api/data', (req, res) => {
  res.json({ data: [1, 2, 3, 4, 5] });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
