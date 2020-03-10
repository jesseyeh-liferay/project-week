# learn_sql

<details open>
  <summary>Sections</summary>

  * [0. SELECT Basics](#0-select-basics)
  * [1. SELECT Names](#1-select-names)
  * [2. SELECT from WORLD](#2-select-from-world)
  * [3. SELECT from Nobel](#3-select-from-nobel)
  * [4. SELECT within SELECT](#4-select-within-select)
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