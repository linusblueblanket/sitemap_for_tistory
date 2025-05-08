export default async function handler(req, res) {
  const response = await fetch(
    'https://raw.githubusercontent.com/linusblueblanket/sitemap_for_tistory/main/sitemap.xml',
    {
      headers: {
        'User-Agent': req.headers['user-agent'] || 'Vercel-Proxy',
      },
    }
  );

  const xml = await response.text();

  res.setHeader('Content-Type', 'application/xml; charset=utf-8');
  res.status(200).send(xml);
}
