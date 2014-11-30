import read_excel
import dal

list_mv = read_excel.get_list_movements()
#save.initialize_db()
dal.save_movements(list_mv)
