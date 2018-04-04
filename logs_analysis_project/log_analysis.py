#!/usr/bin/env python3

import psycopg2

qry_strings = {'most_popular_articles':
               """SELECT articles.title as title, count(title) as num
                  FROM log LEFT JOIN articles on log.path
                  ILIKE '%\' || substring(replace(regexp_replace(articles.title, 
                  '[^a-zA-Z0-9 ]', ''), ' ', '-') from '\w+-\w+-\w+')
                  GROUP BY title
                  ORDER BY num desc limit 3;""",
               'most_popular_authors':
               """SELECT authors.name, count(*) AS cnt
                  FROM articles INNER JOIN authors ON
                  articles.author = authors.id INNER JOIN
                  log on log.path = concat('/article/', articles.slug)
                  WHERE log.status = '200 OK'
                  GROUP BY authors.name
                  ORDER BY cnt desc;""",
                'errors_gt_one_pct':
                """SELECT daily404.day1,
                   (daily404.freq/requests.totreq::float)*100 AS pct
                   FROM ((SELECT log.time::date as day1, count(*) AS freq
                   FROM log WHERE status LIKE '404%' GROUP BY day1
                   ) daily404
                   FULL JOIN (SELECT log.time::date AS day2, count(status) AS
                   totreq FROM log GROUP BY day2
                   ) requests
                   ON daily404.day1 = requests.day2)
                   WHERE daily404.freq/requests.totreq::float > 0.01;"""
               }


def run_query(qry):
    '''create and execute a query in PostgresSQL connection
    :param qry:  a qualified query string.
    '''
    # connect to the database
    db = psycopg2.connect("dbname=news")
    # create a cursor
    cur = db.cursor()
    try:
        if qry:
            # execute the desired query
            cur.execute(qry)
            rst = cur.fetchall()
            return rst
        else:
            print("The query value must be provided.")
    except RuntimeException:
        print("Error, could not execute the desired query.")
    finally:
        # close the connection and return the result
        db.close()


if __name__ == '__main__':
    # create a file named 'output.txt' for writing and output the results
    # from the three query functions above.
    with open('output.txt', 'w') as f:
        # write the first heading
        f.write("3 most popular articles of all time ...")
        f.write('\n')
        rst = run_query(qry_strings['most_popular_articles'])
        # write the first query results to file
        for result in rst:
            f.write('Article: {} -- {} views'.format(result[0], result[1]))
            f.write("\n")
        f.write('\n')
        # write the second heading
        f.write("Most popular article authors of all time ...")
        f.write('\n')
        rst = run_query(qry_strings['most_popular_authors'])
        # write the second query results to the file
        for result in rst:
            f.write('Author: {} -- {} views'.format(result[0], result[1]))
            f.write("\n")
        f.write('\n')
        # write the third heading
        f.write("Days where errors are greater than 1%...")
        f.write('\n')
        rst = run_query(qry_strings['errors_gt_one_pct'])
        # write the thrid query results to the file
        for result in rst:
            f.write("Date: {} -- {}% errors".format(result[0], result[1]))
            f.write('\n')
    # close the file
    f.close()
