# 作者
# NATURE
# 日期
# 2022/12/5 14:38
# 功能
#
import xlrd2
import xlwt


def read_excel(file):
    # 打开文件
    workBook = xlrd2.open_workbook(file);

    # 1.获取sheet的名字
    # 1.1 获取所有sheet的名字(list类型)
    allSheetNames = workBook.sheet_names();
    print(allSheetNames);

    # 1.2 按索引号获取sheet的名字（string类型）
    sheet1Name = workBook.sheet_names()[0];
    print(sheet1Name);

    # 2. 获取sheet内容
    ## 2.1 法1：按索引号获取sheet内容
    sheet1_content1 = workBook.sheet_by_index(0);  # sheet索引从0开始
    ## 2.2 法2：按sheet名字获取sheet内容
    sheet1_content2 = workBook.sheet_by_name(allSheetNames[0]);

    # 3. sheet的名称，行数，列数
    print(sheet1_content1.name, sheet1_content1.nrows, sheet1_content1.ncols);

    # 4. 获取整行和整列的值（数组）
    rows = sheet1_content1.row_values(0);  # 获取第一行内容
    cols = sheet1_content1.col_values(0);  # 获取第一列内容
    print(rows);
    print(cols);

    # 5. 获取单元格内容(三种方式)
    print(sheet1_content1.cell(1, 0).value);
    print(sheet1_content1.cell_value(2, 2));
    print(sheet1_content1.row(2)[2].value);

    # 6. 获取单元格内容的数据类型
    # Tips: python读取excel中单元格的内容返回的有5种类型 [0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error]
    print(sheet1_content1.cell(1, 0).ctype);


def read_xlsx(file, sheet_index=0, sheet_name='sheet1'):
    workBook = xlrd2.open_workbook(file);
    sheet_content = workBook.sheet_by_index(sheet_index)
    rows = sheet_content.nrows
    d = {}
    for i in range(1, rows):
        row_content = sheet_content.row_values(i)
        key, value = row_content[0], row_content[1:3]
        d[key] = value
    return d


if __name__ == '__main__':
    file = r'../data/wxgd.xlsx'
    read_xlsx(file)

    # read_excel(file)
