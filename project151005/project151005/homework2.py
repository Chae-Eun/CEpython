#과제로 예외처리 연습
import sys

try:
    import xlsxwriter
    
    def make():

        fileName = "201401.txt" # 기본 데이터
        field_data = [] # 3번째 필드 리스트
    
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

        newfile = xlsxwriter.Workbook(select+'.xlsx') # 뽑아낸 데이터 엑셀 파일
        worksheet = newfile.add_worksheet() # 엑셀 파일 워크시트 만들어주기
        row = 0 # xlsx 파일에서 행 위치
        col = 0 # xlsx 파일에서 열 위치

        with open(fileName, "r") as myFile :
            for line in myFile:       
                (a, b, c, d, e) = line.split("|") # |로 문자열 나누기

                if select.upper() == c : # 입력값과 c값이 같은 라인 출력
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