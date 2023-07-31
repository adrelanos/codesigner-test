= Notes =

`hello.exe_signed` was created using github actions (CI) and codesigner.

```
osslsigncode verify -in hello.exe_signed
```

```
osslsigncode extract-signature -in hello.exe_signed -out hello.exe_signature
```

```
osslsigncode remove-signature -in hello.exe_signed -out hello.exe_removed
```

```
diff hello.exe hello.exe_removed
```

```
vbindiff hello.exe hello.exe_removed
```

```
diffoscope hello.exe hello.exe_removed
```

```
osslsigncode attach-signature -sigin hello.exe_signature -in hello.exe -out hello.exe_reattached
```
