import pytest
from unittest.mock import patch, MagicMock, call

from patch_mock_test.modules import Examples

class TestExample:
    def test_using_cache(self):
        mock_lib = MagicMock()

        # MagicMockでExample classの中で使われているExampleCacheを置き換える
        with patch("patch_mock_test.modules.ExampleCache", return_value=mock_lib):
            example = Examples()
            example.add(1,2)

        mock_lib.set_cache.assert_called()

        # set_cacheが一回だけ呼ばれているかの確認
        assert mock_lib.set_cache.call_count == 1

        # set_cacheが呼ばれた時の引数を確認する
        args, kwargs = mock_lib.set_cache.call_args
        assert args[0] == "1+2"
        assert args[1] == 3

    def test_using_cache_multi_called(self):
        mock_lib = MagicMock()

        # MagicMockでExample classの中で使われているExampleCacheを置き換える
        with patch("patch_mock_test.modules.ExampleCache", return_value=mock_lib):
            example = Examples()
            example.add(1,2)
            example.add(2,3)
            example.add(3,4)

        # 複数回呼ばれた際に全てのパターンで呼ばれているか検証する
        mock_lib.set_cache.assert_has_calls([call('1+2',3), call('2+3',5), call('3+4', 7)], any_order=True)