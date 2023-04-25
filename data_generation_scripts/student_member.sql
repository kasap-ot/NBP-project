--zemi od end_user, 10000 i stavi gi vo students
INSERT INTO student (id)
SELECT id
FROM generate_series(1,10000) s(i)
CROSS JOIN LATERAL (
  SELECT id
  FROM end_user
  ORDER BY random()
  LIMIT 10000
) AS id
ON CONFLICT (id) DO NOTHING;

--ostatantite 1580 end_user napravi gi members
insert into member (id)
select id
from generate_series(1,10000) s(i) cross join lateral
(select end_user.id from end_user
    left join student s2 on end_user.id = s2.id
    where s2.id is null
    order by random()
    limit 1580) as id
ON CONFLICT (id) DO NOTHING;

--dodadi 400 studenti vo members, i members da se 1980
insert into member(id)
select id
from generate_series(1,10000) s(i) cross join lateral
(select student.id from student
    order by random()
    limit 400) as id
on conflict (id) do nothing;

--proverka
select end_user.id, s2.id as student, m.id from end_user
    left join student s2 on end_user.id = s2.id
    left join member m on end_user.id = m.id;












