import sys
sys.path.append("../..")
from db.utils.dao import *
from db.domain.domain_Y import *
from db.DaoImpl.daoImpl_Y import *

IllustrationID="001"
IllustrationDescription="good"
IllustrationName="ins_1"
node=Illustration(IllustrationID,IllustrationDescription,IllustrationName)
IllustrationDaoImpl.insert(node)
temp=IllustrationDaoImpl.select("001")
temp.output()

newnode=Illustration("001","bad","ins_2")
temp=IllustrationDaoImpl.update(newnode)
temp=IllustrationDaoImpl.update(newnode)
temp.output()

IllustrationDaoImpl.delete("001")
temp=IllustrationDaoImpl.update(newnode)
temp.output()

