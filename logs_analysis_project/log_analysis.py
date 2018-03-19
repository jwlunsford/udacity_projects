#!/usr/bin/env python3

import psycopg2


def most_popular_articles():
    '''create and execute a query that finds the three most popular
    articles'''
    # connect to the database
    db = psycopg2.connect("dbname=news")
    # create a cursor
    cur = db.cursor()
    qryparts = ["SELECT path, count(path) AS cnt FROM log GROUP BY path",
                "HAVING path LIKE '/article%' ORDER BY cnt desc limit 3;"]
    # rejoin the qryparts list
    this_qry = ' '.join(qryparts)
    # execute the desired query
    cur.execute(this_qry)
    rst = cur.fetchall()
    # close the connection and return the result
    db.close()
    return rst
    
    
def most_popular_author():
    '''create and execute a query that finds the most popular authors
    by the total number of articles they've written.'''
    # connect to the database
    db = psycopg2.connect("dbname=news")
    # create a cursor
    cur = db.cursor()
    qryparts = ["SELECT authors.name, count(*) AS cnt"
                "FROM articles INNER JOIN authors ON",
                "articles.author = authors.id INNER JOIN",
                "log on log.path = concat('/article/', articles.slug)",
                "WHERE log.status = '200 OK'",
                "GROUP BY authors.name",
                "ORDER BY cnt desc;"]
    # rejoin the qryparts list
    this_qry = ' '.join(qryparts)
    # execute the desired query
    cur.execute(this_qry)
    rst = cur.fetchall()
    # close the connection and return the result
    db.close()
    return rst
    
    
def request_errors_gt_one_pct():
    '''create and execute a query that finds the date or dates where the
    404 errors are more than 1% of the total page views.'''
    # connect to the database
    db = psycopg2.connect("dbname=news")
    # create a cursor
    cur = db.cursor()
    qryparts = ["SELECT daily404.day1, daily404.freq, requests.totreq,",
                "(daily404.freq/requests.totreq::float)*100 AS pct",
                "FROM ((SELECT log.time::date as day1, count(*) AS freq",
                "FROM log WHERE status LIKE '404%' GROUP BY day1",
                ") daily404",
                "FULL JOIN (SELECT log.time::date AS day2, count(status) AS",
                "totreq FROM log GROUP BY day2",
                ") requests",
                "ON daily404.day1 = requests.day2)",
                "WHERE daily404.freq/requests.totreq::float > 0.01;"]
    # rejoin the qryparts list
    this_qry = ' '.join(qryparts)
    # execute the query
    cur.execute(this_qry)
    rst = cur.fetchall()
    # close the connection and return the result
    db.close()
    return rst
    
    
if __name__ == '__main__':
    # create a file named 'output.txt' for writing and output the results
    # from the three query functions above.
    with open('output.txt', 'w') as f:
        # write the first heading
        f.write("3 most popular articles of all time ...")
        f.write('\n')
        rst = most_popular_articles()
        # write the first query results to file
        for result in rst:
            f.write('Article: {}, {} views'.format(result[0], result[1]))
            f.write("\n")
        f.write('\n')
        # write the second heading
        f.write("Most popular article authors of all time ...")
        f.write('\n')
        rst = most_popular_author()
        # write the second query results to the file
        for result in rst:
            f.write('Author: {}, {} views'.format(result[0], result[1]))
            f.write("\n")
        f.write('\n')
        # write the third heading
        f.write("Days where errors are greater than 1%...")
        f.write('\n')
        rst = request_errors_gt_one_pct()
        # write the thrid query results to the file
        for result in rst:
           f.write("Date: {}, {}% errors".format(result[0], result[3]))
           f.write('\n')
    # close the file
    f.close()