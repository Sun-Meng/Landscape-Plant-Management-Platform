import sys
sys.path.append("../..")
from db.utils.dao import *
from db.domain.domain_Y import *
from db.DaoImpl.daoImpl_Y import *
a=IllustrationDaoImpl()
IllustrationID="001"
IllustrationDescription="good"
IllustrationName="ins_1"
node=Illustration(IllustrationID,IllustrationDescription,IllustrationName)
a.insert(node)
temp=a.select("001")
temp.output()

newnode=Illustration("001","bad","ins_2")
temp=a.update(newnode)
temp=a.update(newnode)
temp.output()

a.delete("001")
temp=a.update(newnode)
temp.output()

