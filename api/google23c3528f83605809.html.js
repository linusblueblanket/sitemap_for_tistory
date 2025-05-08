export default function handler(req, res) {
  res.setHeader('Content-Type', 'text/html');
  res.status(200).send('google-site-verification: google23c3528f83605809.html');
}
