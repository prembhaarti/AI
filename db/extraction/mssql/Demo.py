import pymssql
import json
from Dao import *

class Demo:

    def printData(self,vendorId,attributeName,attributeValue):
        # print(row['VENDOR_ID'])
        # SQL_QUERY="SELECT * FROM dbo.DS_HOMESTAY_VERIFICATION WHERE VENDOR_ID= %s and ATTRIBUTE_NAME=%s and ATTRIBUTE_VALUE=%s"
        SQL_QUERY="SELECT * FROM dbo.DS_HOMESTAY_VERIFICATION WHERE VENDOR_ID= %s and ATTRIBUTE_NAME=%s and ATTRIBUTE_VALUE=%s"
        # SQL_QUERY="SELECT * FROM dbo.DS_HOMESTAY_VERIFICATION"
        # dao2=Dao('172.16.3.118', 'desiya', '+r@v3|9uru', 'TRAVELGURU')
        x=0
        try:
            connection=pymssql.connect('172.16.3.118', 'desiya', '+r@v3|9uru', 'TRAVELGURU');
            cursor2=connection.cursor(as_dict=True)
            cursor2.execute(SQL_QUERY,(vendorId,attributeName,attributeValue))
            #
            # dao2.closeConnectionWithCursor();
            # dao2.createConnectionWithCursor();
            # cursor2=dao2.getCursor().execute(SQL_QUERY,(vendorId,attributeName,attributeValue))
            if cursor2 is not None:
                for row in cursor2:
                    # print("")
                    x=x+1
            else:
                print ("Not found: vendorId:%s, attributeName:%s, attributeValue:%s", vendorId, attributeName, attributeValue)
            cursor2.close()
            connection.close()
        except Exception:
            print "Exception occured for vendor Id:"+vendorId+" attibute Name:"+attributeName+" attribute Value:"+attributeValue
        # finally:
        #     print "fethed till row"+str(x);

        # dao2.closeConnectionWithCursor();

    def main(self):
        # SQL_READ = "select top 1 * from ds_registered_vendor"
        # dao=Dao('DB-MSSQL-PRIMARY','desiya','@desiya123','TRAVELGURU_STAGE')
        # self.printData(1,'x','y')
        BACK_UP_SQL_QUERY = "SELECT * FROM dbo.DS_HOMESTAY_VERIFICATION_BKP"

        dao=Dao('172.16.3.118','desiya','+r@v3|9uru','TRAVELGURU')

        cursor=dao.getCursorByQuery(BACK_UP_SQL_QUERY)
        if cursor is not None:
            for row in cursor:
                vendorId=row['VENDOR_ID']
                requestJson=row['REQUEST_JSON']
                jsonNode=json.loads(requestJson,strict=False)
                vendorName=jsonNode.get('vendorName')
                if vendorName is not None:
                    self.printData(vendorId,'vendorName',vendorName)
                    # print vendorName
                vendorDesc=jsonNode.get('vendorDesc')
                if vendorDesc is not None:
                    self.printData(vendorId,'vendorDesc',vendorDesc)
                    # print vendorDesc
                thingsToAdd=jsonNode.get('thingsToAdd')
                if thingsToAdd is not None:
                    self.printData(vendorId,'thingsToAdd',thingsToAdd)
                roomName=jsonNode.get('roomName')
                if roomName is not None:
                    self.printData(vendorId,'roomName',roomName)
                add1=jsonNode.get('addLine1')
                add2=jsonNode.get('addLine2')
                if add1 is not None and add2 is not None:
                    self.printData(vendorId,'address',add1+"~"+add2)
                elif add1 is not None and add2 is None:
                    self.printData(vendorId,'address',add1)
                elif add2 is not None and add1 is None:
                    self.printData(vendorId,'address',add2)
                # print(row)
                # address=add1+"~"+add2
                # self.printData(vendorId,)

        dao.closeConnectionWithCursor()

    # def validation(self,row):


demo= Demo()
demo.main()
    # if __name__ == '__main__':
    #     print('script started')
    #     main()
    #     print('script completed')