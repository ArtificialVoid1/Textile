from typing import Callable
import asyncio

class Connection:
    def __init__(self, signal, fn : Callable):
        self._connected = True
        self._signal = signal
        self._fn = fn
        self._next = False
    
    def Disconnect(self):
        if self._connected:
            self._connected = False
            
            if self._signal._handlerListHead == self:
                self._signal._handlerListHead == self._next
            else:
                prev = self._signal._handlerListHead
                while prev and prev._next != self:
                    prev = prev._next
                if prev:
                    prev._next = self._next
    def __getattr__(self, key):
        raise AttributeError(f"Attempt to get Connection::{key} (not a valid member)")

    def __setattr__(self, key, value):
        raise AttributeError(f"Attempt to set Connection::{key} (not a valid member)")

class TxeSignal:
    def __init__(self) -> None:
        self._handlerListHead = False
    
    def Connect(self, fn : Callable) -> Connection:
        connection = Connection(self, fn)
        if self._handlerListHead:
            connection._next = self._handlerListHead
            self._handlerListHead = connection
        else:
            self._handlerListHead = connection
        return connection
    
    def DisconnectAll(self):
        self._handlerListHead = False

    def Fire(self, *args):
        item = self._handlerListHead
        while item:
            if item._connected:
                coro = item._fn(*args)
                if asyncio.iscoroutine(coro):
                    asyncio.run(coro)
                else:
                    raise SyntaxError('Connection function must be a coroutine')
            item = item._next

    def __getattr__(self, key):
        raise AttributeError(f"Attempt to get TxeSignal::{key} (not a valid member)")

    def __setattr__(self, key, value):
        raise AttributeError(f"Attempt to set TxeSignal::{key} (not a valid member)")