SELECT * FROM sproj.validate;

select sum(abs(nltk-sentiment)), sum(abs(flair-sentiment)) from validate;

-- show error
select a.flair_bigger, b.flair_smaller, a.nltk_bigger, b.nltk_smaller
from 
(
 select x.flair_bigger, y.nltk_bigger
 from
 (
	select count(flair) as flair_bigger
	from validate
	where flair>sentiment) as x
inner join
(
	select count(nltk) as nltk_bigger
	from validate
	where nltk>sentiment) as y) as a
inner join
(
 select x.flair_smaller, y.nltk_smaller
 from
 (
	select count(flair) as flair_smaller
	from validate
	where flair<sentiment) as x
inner join
(
	select count(nltk) as nltk_smaller
	from validate
	where nltk<sentiment) as y) as b;
    
    


select id, sentiment, nltk, abs(nltk-sentiment), flair, abs(flair-sentiment)
from validate;


-- queries for data analysis

-- counts of sentiment predictions/real
CREATE VIEW label_counts
AS
SELECT
	'label' as 'type',
    count(*) AS total,
    sum(case when sentiment = 0 then 1 else 0 end) AS negCount,
    sum(case when sentiment = 2 then 1 else 0 end) AS neuCount,
    sum(case when sentiment = 4 then 1 else 0 end) AS posCount
FROM validate;

CREATE VIEW flair_counts
AS
SELECT
	'flair' as 'type',
    count(*) AS total,
    sum(case when flair = 0 then 1 else 0 end) AS negCount,
	sum(case when sentiment = 2 then 1 else 0 end) AS neuCount,
    sum(case when flair = 4 then 1 else 0 end) AS posCount
FROM validate;

CREATE VIEW nltk_counts
AS
SELECT
	'nltk' as 'type',
    count(*) AS total,
    sum(case when nltk = 0 then 1 else 0 end) AS negCount,
    sum(case when sentiment = 2 then 1 else 0 end) AS neuCount,
    sum(case when nltk = 4 then 1 else 0 end) AS posCount
FROM validate;

create table counts (
	`type` varchar(10),
    total int,
    negCount int,
    neuCount int,
    posCount int,
    primary key (`type`));
    
INSERT INTO counts(`type`, total, negCount, neuCount, posCount)
select * from label_counts;
INSERT INTO counts(`type`, total, negCount, neuCount, posCount)
select * from flair_counts;
INSERT INTO counts(`type`, total, negCount, neuCount, posCount)
select * from nltk_counts;

-- Flair accuracy-- counts of sentiment predictions/real
CREATE VIEW
flair_neg
AS
SELECT
	'negCount' as 'label',
    sum(case when sentiment = 0 and flair = 0 then 1 else 0 end) AS negCount,
    sum(case when sentiment = 0 and flair = 2 then 1 else 0 end) AS neuCount,
    sum(case when sentiment = 0 and flair = 4 then 1 else 0 end) AS posCount
FROM validate;

CREATE VIEW flair_neu
AS
SELECT
	'neuCount' as 'label',
    sum(case when sentiment = 2 and flair = 0 then 1 else 0 end) AS negCount,
    sum(case when sentiment = 2 and flair = 2 then 1 else 0 end) AS neuCount,
    sum(case when sentiment = 2 and flair = 4 then 1 else 0 end) AS posCount
FROM validate;

CREATE VIEW flair_pos
AS
SELECT
	'posCount' as 'label',
    sum(case when sentiment = 4 and flair = 0 then 1 else 0 end) AS negCount,
    sum(case when sentiment = 4 and flair = 2 then 1 else 0 end) AS neuCount,
    sum(case when sentiment = 4 and flair = 4 then 1 else 0 end) AS posCount
FROM validate;

create table flair_acc (
	`label` varchar(10),
    negCount int,
    neuCount int,
    posCount int,
    primary key (`label`));
    
INSERT INTO flair_acc(`label`, negCount, neuCount, posCount)
select * from flair_neg;
INSERT INTO flair_acc(`label`, negCount, neuCount, posCount)
select * from flair_neu;
INSERT INTO flair_acc(`label`, negCount, neuCount, posCount)
select * from flair_pos;

-- nltk accuracy-- counts of sentiment predictions/real
CREATE VIEW
nltk_neg
AS
SELECT
	'negCount' as 'label',
    sum(case when sentiment = 0 and nltk = 0 then 1 else 0 end) AS negCount,
    sum(case when sentiment = 0 and nltk = 2 then 1 else 0 end) AS neuCount,
    sum(case when sentiment = 0 and nltk = 4 then 1 else 0 end) AS posCount
FROM validate;

CREATE VIEW nltk_neu
AS
SELECT
	'neuCount' as 'label',
    sum(case when sentiment = 2 and nltk = 0 then 1 else 0 end) AS negCount,
    sum(case when sentiment = 2 and nltk = 2 then 1 else 0 end) AS neuCount,
    sum(case when sentiment = 2 and nltk = 4 then 1 else 0 end) AS posCount
FROM validate;

CREATE VIEW nltk_pos
AS
SELECT
	'posCount' as 'label',
    sum(case when sentiment = 4 and nltk = 0 then 1 else 0 end) AS negCount,
    sum(case when sentiment = 4 and nltk = 2 then 1 else 0 end) AS neuCount,
    sum(case when sentiment = 4 and nltk = 4 then 1 else 0 end) AS posCount
FROM validate;

create table nltk_acc (
	`label` varchar(10),
    negCount int,
    neuCount int,
    posCount int,
    primary key (`label`));
    
INSERT INTO nltk_acc(`label`, negCount, neuCount, posCount)
select * from nltk_neg;
INSERT INTO nltk_acc(`label`, negCount, neuCount, posCount)
select * from nltk_neu;
INSERT INTO nltk_acc(`label`, negCount, neuCount, posCount)
select * from nltk_pos;