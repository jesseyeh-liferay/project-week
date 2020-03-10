# learn_sql

<details open>
  <summary>Sections</summary>

  * [0. SELECT Basics](#0-select-basics)
  * [1. SELECT Names](#1-select-names)
  * [2. SELECT from WORLD](#2-select-from-world)
  * [3. SELECT from Nobel](#3-select-from-nobel)
  * [4. SELECT within SELECT](#4-select-within-select)
  * [5. SUM and COUNT](#5-sum-and-count)
  * [6. JOIN](#6-join)
  * [7. More JOIN Operations](#7-more-join-operations)
  * [8. Using Null](#8-using-null)
  * [8+. Numeric Examples](#8-numeric-examples)
  * [9-. Window Function](#9--window-function)
</details>

## 0. SELECT Basics

**1. Selects the row entry in which the name field is "Germany"**
```sql
SELECT population FROM world
  WHERE name = 'Germany'
```
<details>
  <summary>Results</summary>

  | population |
  | ---------- |
  | 80716000   |
</details>

**2. Selects the row entries specified by the list**
```sql
SELECT name, population FROM world
  WHERE name IN ('Brazil', 'Russia', 'India', 'China');
```
<details>
  <summary>Results</summary>

  | name   | population |
  | ------ | ---------- |
  | Brazil | 202794000  |
  | China  | 1365370000 |
  | India  | 1246160000 |
  | Russia | 146000000  |
</details>

**3. Selects the row entries in which the field value matches the specified range (inclusive)**
```sql
SELECT name, area FROM world
  WHERE area BETWEEN 200000 AND 250000
```
<details>
  <summary>Results</summary>

  | name           | area   |
  | -------------- | ------ |
  | Belarus        | 207600 |
  | Ghana          | 238533 |
  | Guinea         | 245857 |
  | Guyana         | 214969 |
  | Laos           | 236800 |
  | Romania        | 238391 |
  | Uganda         | 241550 |
  | United Kingdom | 242900 |
</details>

## 1. SELECT Names

**1. Selects the row entries in which the name field starts with a 'Y'**
```sql
SELECT name FROM world
  WHERE name LIKE 'Y%'
```
<details>
  <summary>Results</summary>

  | name  |
  | ----- |
  | Yemen |
</details>

**7. Selects the row entries in which the name field has three or more 'a's**
```sql
SELECT name FROM world
  WHERE name LIKE '%a%a%a%'
```
<details>
  <summary>Results</summary>

  | name                             |
  | -------------------------------- |
  | Central African Republic         |
  | Equatorial Guinea                |
  | Madagascar                       |
  | Mauritania                       |
  | Tanzania                         |
  | Afghanistan                      |
  | Azerbaijan                       |
  | Malaysia                         |
  | Saudi Arabia                     |
  | United Arab Emirates             |
  | Antigua and Barbuda              |
  | Bahamas                          |
  | Jamaica                          |
  | Trinidad and Tobago              |
  | Albania                          |
  | Bosnia and Herzegovina           |
  | Kazakhstan                       |
  | Canada                           |
  | Guatemala                        |
  | Nicaragua                        |
  | Panama                           |
  | Australia                        |
  | Marshall Islands                 |
  | Micronesia, Federated States of  |
  | Papua New Guinea                 |
  | Paraguay                         |
  | Saint Vincent and the Grenadines |
</details>

**8. `_` is like `%`, but only represents a single character**
```sql
SELECT name FROM world
  WHERE name LIKE '_t%'
ORDER BY name
```
<details>
  <summary>Results</summary>

  | name     |
  | -------- |
  | Ethiopia |
  | Italy    |
</details>

**12. Selects the row entries in which the country's capital is of the form `<Name of country> City`**
```sql
SELECT name FROM world
  WHERE capital LIKE concat(name, '%City')
```
<details>
  <summary>Results</summary>

  | name      |
  | --------- |
  | Guatemala |
  | Kuwait    |
  | Mexico    |
  | Panama    |
</details>

`REPLACE(f, s1, s2)` replaces all occurrences of s1 in f with s2

**15. Selects the row entries in which the name of the capital is the country name followed by an extension, e.g., Monaco (name) followed by -Ville (extension)**
```sql
select name, replace(capital, name, '') from world where capital like concat(name, '_%')
```
<details>
  <summary>Results</summary>

  | name      | replace(capit.. |
  | --------- | --------------- |
  | Andorra   | la Vella        |
  | Guatemala | City            |
  | Kuwait    | City            |
  | Mexico    | City            |
  | Monaco    | \-Ville         |
  | Panama    | City            |
</details>

## 2. SELECT from WORLD

`ROUND(f,p)` rounds f to p decimal places

`LENGTH(s)` returns the number of characters in s

`LEFT(s,n)` returns the first n characters from the start of s

`<>` is the NOT EQUALS operator

## 3. SELECT from Nobel

**13. Selects the row entries in which the winners have "Sir" in their name, ordered first by most recent year, then in alphabetical order**
```sql
select winner, yr, subject from nobel where winner like 'sir %' order by yr desc, winner
```
<details>
  <summary>Results</summary>

  | winner                      | yr   | subject   |
  | --------------------------- | ---- | --------- |
  | Sir Martin J. Evans         | 2007 | Medicine  |
  | Sir Peter Mansfield         | 2003 | Medicine  |
  | Sir Paul Nurse              | 2001 | Medicine  |
  | Sir Harold Kroto            | 1996 | Chemistry |
  | Sir James W. Black          | 1988 | Medicine  |
  | Sir Arthur Lewis            | 1979 | Economics |
  | Sir Nevill F. Mott          | 1977 | Physics   |
  | Sir Bernard Katz            | 1970 | Medicine  |
  | Sir John Eccles             | 1963 | Medicine  |
  | Sir Frank Macfarlane Burnet | 1960 | Medicine  |
  | Sir Cyril Hinshelwood       | 1956 | Chemistry |
  | Sir Robert Robinson         | 1947 | Chemistry |
  | Sir Alexander Fleming       | 1945 | Medicine  |
  | Sir Howard Florey           | 1945 | Medicine  |
  | Sir Henry Dale              | 1936 | Medicine  |
  | Sir Norman Angell           | 1933 | Peace     |
  | Sir Charles Sherrington     | 1932 | Medicine  |
  | Sir Venkata Raman           | 1930 | Physics   |
  | Sir Frederick Hopkins       | 1929 | Medicine  |
  | Sir Austen Chamberlain      | 1925 | Peace     |
  | Sir William Ramsay          | 1904 | Chemistry |
</details>

## 4. SELECT within SELECT

**1. Returns all countries with a population larger than that of Russia's**
```sql
select name from world where population > (select population from world where name = 'russia')
```
<details>
  <summary>Results</summary>

  | name          |
  | ------------- |
  | Bangladesh    |
  | Brazil        |
  | China         |
  | India         |
  | Indonesia     |
  | Nigeria       |
  | Pakistan      |
  | United States |
</details>

**6. Use `ALL` to allow `>`, `<`, `>=`, and `<=` to act over a list**
```sql
select name from world
  where gdp > all(select gdp from world
  	                where continent = 'europe' and gdp >= 0) and continent != 'europe'
```
<details>
  <summary>Results</summary>

  | name          |
  | ------------- |
  | China         |
  | Japan         |
  | United States |
</details>

**7. Use a correlated (a.k.a synchronized) sub-query to allow for two different uses on the same table**
```sql
select continent, name, area from world x
  where area >= all(select area from world y
                      where x.continent = y.continent and area > 0)
```
<details>
  <summary>Results</summary>

  | continent     | name       | area     |
  | ------------- | ---------- | -------- |
  | Africa        | Algeria    | 2381741  |
  | Oceania       | Australia  | 7692024  |
  | South America | Brazil     | 8515767  |
  | North America | Canada     | 9984670  |
  | Asia          | China      | 9596961  |
  | Caribbean     | Cuba       | 109884   |
  | Europe        | Kazakhstan | 2724900  |
  | Eurasia       | Russia     | 17125242 |
</details>

**8. Selects the first country of each continent (alphabetically)**
```sql
select continent, name from world x
  where name <= all(select name from world y
                      where x.continent = y.continent)
```
<details>
  <summary>Results</summary>

  | continent     | name                |
  | ------------- | ------------------- |
  | Africa        | Algeria             |
  | Asia          | Afghanistan         |
  | Caribbean     | Antigua and Barbuda |
  | Eurasia       | Armenia             |
  | Europe        | Albania             |
  | North America | Belize              |
  | Oceania       | Australia           |
  | South America | Argentina           |
</details>

**9. Returns countries in which each other country from the same continent has a population <= 25000000**
```sql
select name, continent, population from world x
  where 25000000 > all(select population from world y
                         where x.continent = y.continent and y.population)
```
<details>
  <summary>Results</summary>

  | name                            | continent | population |
  | ------------------------------- | --------- | ---------- |
  | Antigua and Barbuda             | Caribbean | 86295      |
  | Australia                       | Oceania   | 23545500   |
  | Bahamas                         | Caribbean | 351461     |
  | Barbados                        | Caribbean | 285000     |
  | Cuba                            | Caribbean | 11167325   |
  | Dominica                        | Caribbean | 71293      |
  | Dominican Republic              | Caribbean | 9445281    |
  | Fiji                            | Oceania   | 858038     |
  | Grenada                         | Caribbean | 103328     |
  | Haiti                           | Caribbean | 10413211   |
  | Jamaica                         | Caribbean | 2717991    |
  | Kiribati                        | Oceania   | 106461     |
  | Marshall Islands                | Oceania   | 56086      |
  | Micronesia, Federated States of | Oceania   | 101351     |
  | Nauru                           | Oceania   | 9945       |
  | New Zealand                     | Oceania   | 4538520    |
  | Palau                           | Oceania   | 20901      |
  | Papua New Guinea                | Oceania   | 7398500    |
  | Saint Lucia                     | Caribbean | 180000     |
  | Samoa                           | Oceania   | 187820     |
  | Solomon Islands                 | Oceania   | 581344     |
  | Tonga                           | Oceania   | 103036     |
  | Trinidad and Tobago             | Caribbean | 1328019    |
  | Tuvalu                          | Oceania   | 11323      |
  | Vanuatu                         | Oceania   | 264652     |
</details>

**10. Returns countries whose populations are 3x greater than all other countries within the same continent**
```sql
select name, continent from world x
  where population > all(select 3 * population from world y
                           where x.continent = y.continent and y.population > 0 and x.name != y.name)
```
<details>
  <summary>Results</summary>

  | name      | continent     |
  | --------- | ------------- |
  | Australia | Oceania       |
  | Brazil    | South America |
  | Russia    | Eurasia       |
</details>

## 5. SUM and COUNT

**1. Returns the sum of all populations**
```sql
SELECT SUM(population)
FROM world
```
<details>
  <summary>Results</summary>

  | SUM(populatio.. |
  | --------------- |
  | 7118632738      |
</details>

**2. Returns a row entry for each unique continent**
```sql
select distinct(continent) from world
```
<details>
  <summary>Results</summary>

  | continent     |
  | ------------- |
  | Africa        |
  | Asia          |
  | Caribbean     |
  | Eurasia       |
  | Europe        |
  | North America |
  | Oceania       |
  | South America |
</details>

**4. Returns the number of countries that satisfy the minimum area specification**
```sql
select count(*) from world where area >= 1000000
```
<details>
  <summary>Results</summary>

  | count(\*) |
  | --------- |
  | 29        |
</details>

**6. Returns the number of countries in each continent**
```sql
select continent, count(name) from world group by continent
```
<details>
  <summary>Results</summary>

  | continent     | count(name) |
  | ------------- | ----------- |
  | Africa        | 53          |
  | Asia          | 47          |
  | Caribbean     | 11          |
  | Eurasia       | 2           |
  | Europe        | 44          |
  | North America | 11          |
  | Oceania       | 14          |
  | South America | 13          |
</details>

**8. The `WHERE` clause filters rows before aggregation, whereas the `HAVING` clause filters afterwards**
```sql
select continent from world group by continent having sum(population) > 100000000
```
<details>
  <summary>Results</summary>

  | continent     |
  | ------------- |
  | Africa        |
  | Asia          |
  | Eurasia       |
  | Europe        |
  | North America |
  | South America |
</details>

## 6. JOIN

`JOIN` allows for the use of data from two or more tables

**3. Combines two different tables to show data on every German goal**
```sql
SELECT player,teamid,stadium,mdate
  FROM game JOIN goal ON (id=matchid) where teamid='ger'
```
<details>
  <summary>Results</summary>

  | player         | teamid | stadium                  | mdate        |
  | -------------- | ------ | ------------------------ | ------------ |
  | Mario Gómez    | GER    | Arena Lviv               | 9 June 2012  |
  | Mario Gómez    | GER    | Metalist Stadium         | 13 June 2012 |
  | Mario Gómez    | GER    | Metalist Stadium         | 13 June 2012 |
  | Lukas Podolski | GER    | Arena Lviv               | 17 June 2012 |
  | Lars Bender    | GER    | Arena Lviv               | 17 June 2012 |
  | Philipp Lahm   | GER    | PGE Arena Gdansk         | 22 June 2012 |
  | Sami Khedira   | GER    | PGE Arena Gdansk         | 22 June 2012 |
  | Miroslav Klose | GER    | PGE Arena Gdansk         | 22 June 2012 |
  | Marco Reus     | GER    | PGE Arena Gdansk         | 22 June 2012 |
  | Mesut Özil     | GER    | National Stadium, Warsaw | 28 June 2012 |
</details>

**13. Returns a scoreboard**
```sql
SELECT mdate,
  team1,
  sum(CASE WHEN teamid=team1 THEN 1 ELSE 0 END) as score1,
  team2,
  sum(CASE WHEN teamid=team2 THEN 1 ELSE 0 END) as score2
  FROM game LEFT JOIN goal ON matchid = id
group by mdate, team1, team2
order by mdate, matchid, team1, team2
```
<details>
  <summary>Results</summary>

  | mdate        | team1 | score1 | team2 | score2 |
  | ------------ | ----- | ------ | ----- | ------ |
  | 1 July 2012  | ESP   | 4      | ITA   | 0      |
  | 10 June 2012 | ESP   | 1      | ITA   | 1      |
  | 10 June 2012 | IRL   | 1      | CRO   | 3      |
  | 11 June 2012 | FRA   | 1      | ENG   | 1      |
  | 11 June 2012 | UKR   | 2      | SWE   | 1      |
  | 12 June 2012 | GRE   | 1      | CZE   | 2      |
  | 12 June 2012 | POL   | 1      | RUS   | 1      |
  | 13 June 2012 | DEN   | 2      | POR   | 3      |
  | 13 June 2012 | NED   | 1      | GER   | 2      |
  | 14 June 2012 | ITA   | 1      | CRO   | 1      |
  | 14 June 2012 | ESP   | 4      | IRL   | 0      |
  | 15 June 2012 | UKR   | 0      | FRA   | 2      |
  | 15 June 2012 | SWE   | 2      | ENG   | 3      |
  | 16 June 2012 | CZE   | 1      | POL   | 0      |
  | 16 June 2012 | GRE   | 1      | RUS   | 0      |
  | 17 June 2012 | POR   | 2      | NED   | 1      |
  | 17 June 2012 | DEN   | 1      | GER   | 2      |
  | 18 June 2012 | CRO   | 0      | ESP   | 1      |
  | 18 June 2012 | ITA   | 2      | IRL   | 0      |
  | 19 June 2012 | ENG   | 1      | UKR   | 0      |
  | 19 June 2012 | SWE   | 2      | FRA   | 0      |
  | 21 June 2012 | CZE   | 0      | POR   | 1      |
  | 22 June 2012 | GER   | 4      | GRE   | 2      |
  | 23 June 2012 | ESP   | 2      | FRA   | 0      |
  | 24 June 2012 | ENG   | 0      | ITA   | 0      |
  | 27 June 2012 | POR   | 0      | ESP   | 0      |
  | 28 June 2012 | GER   | 1      | ITA   | 2      |
  | 8 June 2012  | POL   | 1      | GRE   | 1      |
  | 8 June 2012  | RUS   | 4      | CZE   | 1      |
  | 9 June 2012  | NED   | 0      | DEN   | 1      |
  | 9 June 2012  | GER   | 1      | POR   | 0      |
</details>

## 7. More JOIN Operations

**10. Joins three tables to list all 1962 films with their leading stars**
```sql
select title, name
from movie join casting on (id=movieid) join actor on (actorid=actor.id)
where ord=1 and yr=1962
```
<details>
  <summary>Results</summary>

  | title                                                      | name                       |
  | ---------------------------------------------------------- | -------------------------- |
  | A Kind of Loving                                           | Alan Bates                 |
  | A Symposium on Popular Songs                               | Paul Frees                 |
  | A Very Private Affair (Vie PrivÃ©e)                        | Brigitte Bardot            |
  | An Autumn Afternoon                                        | Chishu Ryu                 |
  | Atraco a las tres                                          | JosÃ© Luis LÃ³pez VÃ¡zquez |
  | Barabbas                                                   | Anthony Quinn              |
  | Battle Beyond the Sun (ÐÐµÐ±Ð¾ Ð·Ð¾Ð²ÐµÑ‚)                | Aleksandr Shvorin          |
  | Big and Little Wong Tin Bar                                | Jackie Chan                |
  | Billy Budd                                                 | Terence Stamp              |
  | Billy Rose's Jumbo                                         | Doris Day                  |
  | Birdman of Alcatraz                                        | Burt Lancaster             |
  | Boccaccio '70                                              | Anita Ekberg               |
  | Bon Voyage!                                                | Fred MacMurray             |
  | Boys' Night Out                                            | Kim Novak                  |
  | Cape Fear                                                  | Gregory Peck               |
  | Carnival of Souls                                          | Candace Hilligoss          |
  | Carry On Cruising                                          | Sid James                  |
  | David and Lisa                                             | Keir Dullea                |
  | Days of Wine and Roses                                     | Jack Lemmon                |
  | Dr. No                                                     | Sean Connery               |
  | L'Eclisse                                                  | Alain Delon                |
  | Tutti a casa                                               | Alberto Sordi              |
  | Experiment in Terror                                       | Glenn Ford                 |
  | Eyes Without a Face                                        | Pierre Brasseur            |
  | Gay Purr-ee                                                | Judy Garland               |
  | Gigot                                                      | Jackie Gleason             |
  | Gorath                                                     | Ryo Ikebe                  |
  | Gypsy                                                      | Rosalind Russell           |
  | Half Ticket                                                | Kishore Kumar              |
  | Harakiri                                                   | Tatsuya Nakadai            |
  | In Search of the Castaways                                 | Hayley Mills               |
  | It's Only Money                                            | Jerry Lewis                |
  | Jigsaw                                                     | Jack Warner                |
  | Kid Galahad                                                | Elvis Presley              |
  | La commare secca                                           | Marisa Solinas             |
  | La notte                                                   | Marcello Mastroianni       |
  | Life for Ruth                                              | Michael Craig              |
  | Lolita                                                     | James Mason                |
  | Long Day's Journey into Night                              | Katharine Hepburn          |
  | Love at Twenty                                             | Jean-Pierre LÃ©aud         |
  | Lycanthropus                                               | Barbara Lass               |
  | Mamma Roma                                                 | Anna Magnani               |
  | Merrill's Marauders                                        | Jeff Chandler              |
  | Mother Joan of the Angels                                  | Lucyna Winnicka            |
  | Mr. Hobbs Takes a Vacation                                 | James Stewart              |
  | Mutiny on the Bounty                                       | Marlon Brando              |
  | On the Beat                                                | Norman Wisdom              |
  | Os Cafajestes                                              | Daniel Filho               |
  | Panic in Year Zero!                                        | Ray Milland                |
  | Period of Adjustment                                       | Anthony Franciosa          |
  | Results truncated. Only the first 50 rows have been shown. |
</details>

**11. Shows the years in which Rock Hudson made more than two movies that year**
```sql
select yr, count(title)
from movie join casting on (movie.id=movieid)
           join actor   on (actorid=actor.id)
where name='rock hudson'
group by yr
having count(title) > 2
```
<details>
  <summary>Results</summary>

  | yr   | count(title) |
  | ---- | ------------ |
  | 1953 | 5            |
  | 1961 | 3            |
</details>

**12. Returns movie titles and their corresponding leading stars from movies in which Julie Andrews was a cast member**
```sql
select title, name
from movie join casting on (movie.id=movieid)
           join actor   on (actorid=actor.id)
where ord=1 and movieid in (select movieid
                            from casting
                            where actorid in (select id
                                              from actor
                                              where name='julie andrews'))
```
<details>
  <summary>Results</summary>

  | title                                    | name           |
  | ---------------------------------------- | -------------- |
  | 10                                       | Dudley Moore   |
  | Darling Lili                             | Julie Andrews  |
  | Despicable Me                            | Steve Carell   |
  | Duet for One                             | Julie Andrews  |
  | Hawaii                                   | Julie Andrews  |
  | Little Miss Marker                       | Walter Matthau |
  | Mary Poppins                             | Julie Andrews  |
  | Relative Values                          | Julie Andrews  |
  | S.O.B.                                   | Julie Andrews  |
  | Shrek the Third                          | Mike Myers     |
  | Star!                                    | Julie Andrews  |
  | The Americanization of Emily             | James Garner   |
  | The Pink Panther Strikes Again           | Peter Sellers  |
  | The Princess Diaries                     | Anne Hathaway  |
  | The Princess Diaries 2: Royal Engagement | Anne Hathaway  |
  | The Sound of Music                       | Julie Andrews  |
  | The Tamarind Seed                        | Julie Andrews  |
  | Thoroughly Modern Millie                 | Julie Andrews  |
  | Tooth Fairy                              | Dwayne Johnson |
  | Torn Curtain                             | Paul Newman    |
  | Victor Victoria                          | Julie Andrews  |
</details>

**14. Returns movies ordered by the number of actors in the cast, then by title**
```sql
select title, count(actorid)
from movie join casting on (id=movieid)
where yr=1978
group by title
order by count(actorid) desc, title
```
<details>
  <summary>Results</summary>

  | title                                                      | count(actorid) |
  | ---------------------------------------------------------- | -------------- |
  | The Bad News Bears Go to Japan                             | 50             |
  | The Swarm                                                  | 37             |
  | Grease                                                     | 28             |
  | American Hot Wax                                           | 27             |
  | The Boys from Brazil                                       | 26             |
  | Heaven Can Wait                                            | 25             |
  | Big Wednesday                                              | 21             |
  | A Night Full of Rain                                       | 19             |
  | A Wedding                                                  | 19             |
  | Orchestra Rehearsal                                        | 19             |
  | The Cheap Detective                                        | 19             |
  | Go Tell the Spartans                                       | 18             |
  | Death on the Nile                                          | 17             |
  | Movie Movie                                                | 17             |
  | Superman                                                   | 17             |
  | The Cat from Outer Space                                   | 17             |
  | The Driver                                                 | 17             |
  | The Star Wars Holiday Special                              | 17             |
  | Blue Collar                                                | 16             |
  | Ice Castles                                                | 16             |
  | International Velvet                                       | 16             |
  | J.R.R. Tolkien's The Lord of the Rings                     | 16             |
  | Alexandria... Why?                                         | 15             |
  | Bye Bye Monkey                                             | 15             |
  | Coming Home                                                | 15             |
  | David                                                      | 15             |
  | Gray Lady Down                                             | 15             |
  | Occupation in 26 Pictures                                  | 15             |
  | Revenge of the Pink Panther                                | 15             |
  | The Brink's Job                                            | 15             |
  | The Chant of Jimmie Blacksmith                             | 15             |
  | The Water Babies                                           | 15             |
  | Violette NoziÃ¨re                                          | 15             |
  | Who'll Stop The Rain                                       | 15             |
  | Without Anesthesia                                         | 15             |
  | Bread and Chocolate                                        | 14             |
  | Closed Circuit                                             | 14             |
  | Damien: Omen II                                            | 14             |
  | I Wanna Hold Your Hand                                     | 14             |
  | The Empire of Passion                                      | 14             |
  | Almost Summer                                              | 13             |
  | An Unmarried Woman                                         | 13             |
  | Foul Play                                                  | 13             |
  | Goin' South                                                | 13             |
  | The Left-Handed Woman                                      | 13             |
  | California Suite                                           | 12             |
  | Force 10 From Navarone                                     | 12             |
  | In Praise of Older Women                                   | 12             |
  | Jaws 2                                                     | 12             |
  | Midnight Express                                           | 12             |
  | Results truncated. Only the first 50 rows have been shown. |
</details>

**15. Returns all cast members who have worked with Art Garfunkel**
```sql
select distinct name
from actor join casting on (id=actorid)
where movieid in (select movie.id -- get all movies associated with art
                  from movie join casting on (id=movieid)
                             join actor   on (actorid=actor.id)
                  where name='art garfunkel')
and name != 'art garfunkel'
```
<details>
  <summary>Results</summary>

  | name                   |
  | ---------------------- |
  | Mark Ruffalo           |
  | Ryan Phillippe         |
  | Mike Myers             |
  | Neve Campbell          |
  | Salma Hayek            |
  | Sela Ward              |
  | Breckin Meyer          |
  | Sherry Stringfield     |
  | Cameron Mathison       |
  | Heather Matarazzo      |
  | Skipp Sudduth          |
  | Lauren Hutton          |
  | Michael York           |
  | Ellen Albertini Dow    |
  | Thelma Houston         |
  | Ron Jeremy             |
  | Elio Fiorucci          |
  | Sheryl Crow            |
  | Georgina Grenville     |
  | Cindy Crawford         |
  | Heidi Klum             |
  | Donald Trump           |
  | Cecilie Thomsen        |
  | Frederique van der Wal |
  | Veronica Webb          |
  | Peter Bogdanovich      |
  | Beverly Johnson        |
  | Bruce Jay Friedman     |
  | Lorna Luft             |
  | Valerie Perrine        |
  | Stars on 54            |
  | Julian Sands           |
  | Bill Paxton            |
  | Sherilyn Fenn          |
  | Kurtwood Smith         |
  | Harris Yulin           |
  | Robert DoQui           |
</details>
