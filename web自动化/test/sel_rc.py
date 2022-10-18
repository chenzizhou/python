# 作者
# NATURE
# 日期
# 2022/10/18 9:37
# 功能
#
import selenium
sel = selenium("localhost",4444,"firefox","http://www.baidu.com/" )
sel .start()
sel .open("/")
sel.type ( "id=kw", "selenium grid")
sel.click ( "id=su")
sel. wait_for_page_to_load ( "30000")
sel.stop ()

