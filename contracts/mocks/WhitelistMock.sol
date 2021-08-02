// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "../Whitelist.sol";

contract WhitelistMock is Whitelist {
    function onlyWhitelistedCanDoThis()
        external
        view
        onlyWhitelisted
        returns (bool)
    {
        return true;
    }
}
