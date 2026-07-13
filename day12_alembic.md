so today we would be talking about alembic in this the alembic is being used in sqlalchemy to 
create , alter , update , delete  the data in the database 
int tutorial section the setup of alembic is being explained
Alembic there is a feature called as autogenerate that can detect several form of changes such as the additon in column , additon in row , removal of foreign key , table additon , change of nullible status , basic changes in foreign key 
--A metadata is also being generated that has all the stored sata of the schema that is all the table objects being stored 
important questions 
1) what is alembic?
it is a tool used to keep up with the database schema and the sqlalchemy 
2)what is migration 
it is making changes in the dtabase 
3)alembi.init is what ? 
it is all the migration files and the alembic config
4) what iaas alembic.ini?
config to database connection and also alembic settings 
5) what is env.py?
so it helps in making all the migrations from sqlalchemy to the alembic software 
6) upgrade 
it is making the changes so that the 
7) downgrade 
it is reverting the changes 
8) whats autogenerte?
Autogenerate is an Alembic feature that automatically generates a migration file by comparing the SQLAlchemy models with the current database schema.

A naming convention automatically generates consistent names for constraints, making Alembic migrations (such as op.drop_constraint()) easier and more reliable.so it generates name by using the tools such as automatic name generation such that pk_users() 

so some of the important point from each para of the header Running “Batch” Migrations for SQLite and Other Databases

1)sqllite does not support alter statment 
2)so the question is how does things workout in sqllite?
so the tables are expected to be copied by migration and then the data is also being moved along so after that the drop table occur this is called copy and move and this is done in lot of volume so branching is used for this 
so this is how alembic does the job 
Old Table (some_table)
        │
        ▼
Create Temporary Table
        │
        ▼
Copy Data
        │
        ▼
Delete Old Table
        │
        ▼
Rename Temporary Table
        │
        ▼
New some_table (updated schema)

in code form the same thing is this 

CREATE TABLE _alembic_batch_temp (
  id INTEGER NOT NULL,
  foo INTEGER,
  PRIMARY KEY (id)
);
INSERT INTO _alembic_batch_temp (id) SELECT some_table.id FROM some_table;
DROP TABLE some_table;
ALTER TABLE _alembic_batch_temp RENAME TO some_table;

there is also a process of reflection so in this we read the sqlalchemy database schema and then load it into sqlalchemy as table 
so some of them are the check constraint these are the the constraints that are being put up to ensure that all the 
rules of database are followed or not . 

named check constraints -- the named check constraint are those that are automatically being present in branch 
unnamed check constraint -- these are those which are not being automatically present in the batch process

Branch -- so this branches are being made in two diffrent direction these could be merged together to form a single file and both the heads of the brancehes could be merged together to get the desired result th structure looks like this 
                            -- ae1027a6acf -->
                           /                   \
<base> --> 1975ea83b712 -->                      --> mergepoint
                           \                   /
                            -- 27c6a30d7c24 -->

so how does this branching occurs is this simply like merging ??
a -- so the branching occurs by the following method first is like the topological sorting thaat occurs is the sorting of various elements into 
-- so here is the list of commands that are being performed using alembic 
| Operation                       | Purpose                                                      |
| ------------------------------- | ------------------------------------------------------------ |
| `op.create_table()`             | Create a new table.                                          |
| `op.drop_table()`               | Delete a table.                                              |
| `op.add_column()`               | Add a new column to an existing table.                       |
| `op.drop_column()`              | Remove a column from a table.                                |
| `op.alter_column()`             | Modify a column (type, nullable, default, name, etc.).       |
| `op.rename_table()`             | Rename a table.                                              |
| `op.create_index()`             | Create an index for faster queries.                          |
| `op.drop_index()`               | Remove an index.                                             |
| `op.create_primary_key()`       | Create a primary key constraint.                             |
| `op.create_foreign_key()`       | Create a foreign key relationship.                           |
| `op.drop_constraint()`          | Remove a constraint (PK, FK, Unique, Check).                 |
| `op.create_unique_constraint()` | Ensure column values are unique.                             |
| `op.create_check_constraint()`  | Add a CHECK constraint.                                      |
| `op.execute()`                  | Execute raw SQL directly.                                    |
| `op.bulk_insert()`              | Insert multiple rows during a migration.                     |
| `op.batch_alter_table()`        | Perform multiple table changes together (mainly for SQLite). |


#practice segment 
op.create_table()
op.drop_table()
op.add_column()
op.alter_column()
op.