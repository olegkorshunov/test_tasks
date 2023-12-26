SELECT * from article
where id not in (SELECT DISTINCT article_id from comment)