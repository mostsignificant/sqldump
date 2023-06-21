import sqldump as dp

dp.dump_to_sql('example/example.csv', 'postgresql://postgres:mysecretpassword@127.0.0.1:5432/postgres')