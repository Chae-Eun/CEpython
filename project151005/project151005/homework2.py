#������ ����ó�� ����
import sys

try:
    import xlsxwriter
    
    def make():

        fileName = "201401.txt" # �⺻ ������
        field_data = [] # 3��° �ʵ� ����Ʈ
    
        with open(fileName, "r") as myFile:
            for line in myFile:
                (a, b, c, d, e) = line.split("|")

                if c not in field_data :
                    field_data.append(c)

        print("-------------------------field name-------------------------")
        for steps in field_data:
            print(steps + " ", end = "")
        print()
        print("------------------------------------------------------------")
        select = input("Select the field name : ")

        newfile = xlsxwriter.Workbook(select+'.xlsx') # �̾Ƴ� ������ ���� ����
        worksheet = newfile.add_worksheet() # ���� ���� ��ũ��Ʈ ������ֱ�
        row = 0 # xlsx ���Ͽ��� �� ��ġ
        col = 0 # xlsx ���Ͽ��� �� ��ġ

        with open(fileName, "r") as myFile :
            for line in myFile:       
                (a, b, c, d, e) = line.split("|") # |�� ���ڿ� ������

                if select.upper() == c : # �Է°��� c���� ���� ���� ���
                    worksheet.write(row, col, a)
                    worksheet.write(row, col+1, b)
                    worksheet.write(row, col+2, c)
                    worksheet.write(row, col+3, d)
                    row += 1

        newfile.close()
        print("Finish! Check the "+select+".xlsx")
except:
    error = sys.exc_info()[0]
    print(error)