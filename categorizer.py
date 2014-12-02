import dal


def categorize():
    categories = dal.get_categories()
    movements = dal.get_uncategorized_movements()
    cat_move = [(c1,m1)
                for m1,m2,m3,m4,m5,m6,_ in movements
                for c1,_,c3 in categories
                if c3.upper() in m3.upper()]

    dal.update_movements(cat_move)


if __name__ == '__main__':
    categorize()
    print "Categorized"
