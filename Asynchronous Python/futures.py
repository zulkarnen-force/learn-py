#pylint: disable = no-value-for-parameter invalid-name

from concurrent.futures import ThreadPoolExecutor as Executor


urls = """google facebook whatsapp instagram""".split()


def fetch(url):
    from urllib import request, error

    try:
        data = request.urlopen(url).read()
        return '{}: length {}'.format(url, len(data))

    except error.HTTPError as why:
        return '{}: {}'.format(url, why)


with Executor(max_workers=4) as exe:
    template = 'http://www.{}.com'
    jobs = [exe.submit(fetch, template.format(u)) for u in urls]
    results = [job.result() for job in jobs]
    print('\n'.join(results))

fetch()
