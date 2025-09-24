from vuln_test import patterns
import tempfile, os

def main():
    print('Running test stubs for each wrapper (no network operations).')

    # torch.load stub
    try:
        tmp = tempfile.NamedTemporaryFile(delete=False)
        tmp_name = tmp.name
        tmp.close()
        try:
            res = patterns.torch_load_weights(tmp_name)
            print('torch_load_weights ->', type(res))
        except Exception as e:
            print('torch_load_weights failed (ok):', e)
        finally:
            try:
                os.unlink(tmp_name)
            except Exception:
                pass
    except Exception as e:
        print('torch test skipped:', e)

    # werkzeug.safe_join
    try:
        print('werkzeug_safe_join ->', patterns.werkzeug_safe_join_wrapper('/tmp', 'a', 'b'))
    except Exception as e:
        print('werkzeug_safe_join failed (ok):', e)

    # feedparser.parse
    try:
        print('feedparser_parse ->', patterns.feedparser_parse_wrapper(''))
    except Exception as e:
        print('feedparser_parse failed (ok):', e)

    # cryptography stub
    try:
        print('cryptography_stub ->', patterns.cryptography_stub_usage())
    except Exception as e:
        print('cryptography_stub failed (ok):', e)

    # nltk.download
    try:
        print('nltk_download ->', patterns.nltk_trigger_download('punkt'))
    except Exception as e:
        print('nltk_download failed (ok):', e)

    # paramiko stub
    try:
        print('paramiko_stub ->', patterns.paramiko_transport_auth_stub())
    except Exception as e:
        print('paramiko_stub failed (ok):', e)

    # zipfile extract
    try:
        zip_path = tempfile.NamedTemporaryFile(delete=False, suffix='.zip').name
        with open(zip_path, 'wb') as f:
            import zipfile as _z
            with _z.ZipFile(f, 'w') as zz:
                zz.writestr('hello.txt', 'hello')
        print('zip_extract ->', patterns.zipfile_extract_wrapper(zip_path, extract_dir='.' ))
        try:
            os.unlink(zip_path)
        except Exception:
            pass
    except Exception as e:
        print('zip extract failed (ok):', e)

if __name__ == '__main__':
    main()
