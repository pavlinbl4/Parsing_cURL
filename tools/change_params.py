import pprint


def change_params(params):
    i = 0
    params['pageprms.pagenum'] = str(i + 1)
    params_new = params
    return params_new


if __name__ == '__main__':
    params_old = {
        'total': '29248',
        'pageprms.pagesize': '80',
        'pageprms.pagenum': '1',
        'csrftoken': '1788c0a9dcd6909e4b40cdf930863e4177af38b8c87717e8da9b903a024205379e7574fffa990d69',
    }
    pprint.pprint(change_params(params_old))
