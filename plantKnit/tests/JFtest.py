import sys
sys.path.append("../..")
from db.utils.Dao_base import *
from db.domain.domain_Y import *
from db.DaoImpl.daoImpl_Y import *

IllustrationID="001"
IllustrationDescription="good"
IllustrationName="ins_1"
node=Illustration(IllustrationID,IllustrationDescription,IllustrationName)
IllustrationDaoImpl.insert(node)


