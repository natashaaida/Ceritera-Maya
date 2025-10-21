
  var Module = typeof Module !== 'undefined' ? Module : {};
  
  if (!Module.expectedDataFileDownloads) {
    Module.expectedDataFileDownloads = 0;
  }
  Module.expectedDataFileDownloads++;
  (function() {
   var loadPackage = function(metadata) {
  
      var PACKAGE_PATH;
      if (typeof window === 'object') {
        PACKAGE_PATH = window['encodeURIComponent'](window.location.pathname.toString().substring(0, window.location.pathname.toString().lastIndexOf('/')) + '/');
      } else if (typeof location !== 'undefined') {
        // worker
        PACKAGE_PATH = encodeURIComponent(location.pathname.toString().substring(0, location.pathname.toString().lastIndexOf('/')) + '/');
      } else {
        throw 'using preloaded data can only be done on a web page or in a web worker';
      }
      var PACKAGE_NAME = 'pyapp.data';
      var REMOTE_PACKAGE_BASE = 'pyapp.data';
      if (typeof Module['locateFilePackage'] === 'function' && !Module['locateFile']) {
        Module['locateFile'] = Module['locateFilePackage'];
        err('warning: you defined Module.locateFilePackage, that has been renamed to Module.locateFile (using your locateFilePackage for now)');
      }
      var REMOTE_PACKAGE_NAME = Module['locateFile'] ? Module['locateFile'](REMOTE_PACKAGE_BASE, '') : REMOTE_PACKAGE_BASE;
    
      var REMOTE_PACKAGE_SIZE = metadata['remote_package_size'];
      var PACKAGE_UUID = metadata['package_uuid'];
    
      function fetchRemotePackage(packageName, packageSize, callback, errback) {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', packageName, true);
        xhr.responseType = 'arraybuffer';
        xhr.onprogress = function(event) {
          var url = packageName;
          var size = packageSize;
          if (event.total) size = event.total;
          if (event.loaded) {
            if (!xhr.addedTotal) {
              xhr.addedTotal = true;
              if (!Module.dataFileDownloads) Module.dataFileDownloads = {};
              Module.dataFileDownloads[url] = {
                loaded: event.loaded,
                total: size
              };
            } else {
              Module.dataFileDownloads[url].loaded = event.loaded;
            }
            var total = 0;
            var loaded = 0;
            var num = 0;
            for (var download in Module.dataFileDownloads) {
            var data = Module.dataFileDownloads[download];
              total += data.total;
              loaded += data.loaded;
              num++;
            }
            total = Math.ceil(total * Module.expectedDataFileDownloads/num);
            if (Module['setStatus']) Module['setStatus']('Downloading data... (' + loaded + '/' + total + ')');
          } else if (!Module.dataFileDownloads) {
            if (Module['setStatus']) Module['setStatus']('Downloading data...');
          }
        };
        xhr.onerror = function(event) {
          throw new Error("NetworkError for: " + packageName);
        }
        xhr.onload = function(event) {
          if (xhr.status == 200 || xhr.status == 304 || xhr.status == 206 || (xhr.status == 0 && xhr.response)) { // file URLs can return 0
            var packageData = xhr.response;
            callback(packageData);
          } else {
            throw new Error(xhr.statusText + " : " + xhr.responseURL);
          }
        };
        xhr.send(null);
      };

      function handleError(error) {
        console.error('package error:', error);
      };
    
    function runWithFS() {
  
      function assert(check, msg) {
        if (!check) throw msg + new Error().stack;
      }
  Module['FS_createPath']("/", "_dummy_thread", true, true);
Module['FS_createPath']("/", "http", true, true);
Module['FS_createPath']("/", "xmlrpc", true, true);
Module['FS_createPath']("/", "_thread", true, true);
Module['FS_createPath']("/", "libpasteurize", true, true);
Module['FS_createPath']("/libpasteurize", "fixes", true, true);
Module['FS_createPath']("/", "six-1.12.0.dist-info", true, true);
Module['FS_createPath']("/", "socketserver", true, true);
Module['FS_createPath']("/", "past", true, true);
Module['FS_createPath']("/past", "builtins", true, true);
Module['FS_createPath']("/past", "types", true, true);
Module['FS_createPath']("/past", "utils", true, true);
Module['FS_createPath']("/past", "translation", true, true);
Module['FS_createPath']("/", "builtins", true, true);
Module['FS_createPath']("/", "libfuturize", true, true);
Module['FS_createPath']("/libfuturize", "fixes", true, true);
Module['FS_createPath']("/", "bin", true, true);
Module['FS_createPath']("/", "ecdsa-0.18.0.dist-info", true, true);
Module['FS_createPath']("/", "html", true, true);
Module['FS_createPath']("/", "ecdsa", true, true);
Module['FS_createPath']("/", "lib", true, true);
Module['FS_createPath']("/lib", "python2.7", true, true);
Module['FS_createPath']("/lib/python2.7", "site-packages", true, true);
Module['FS_createPath']("/lib/python2.7/site-packages", "pygame_sdl2", true, true);
Module['FS_createPath']("/lib/python2.7/site-packages/pygame_sdl2", "threads", true, true);
Module['FS_createPath']("/", "_markupbase", true, true);
Module['FS_createPath']("/", "future-0.18.2.dist-info", true, true);
Module['FS_createPath']("/", "future", true, true);
Module['FS_createPath']("/future", "builtins", true, true);
Module['FS_createPath']("/future", "backports", true, true);
Module['FS_createPath']("/future/backports", "http", true, true);
Module['FS_createPath']("/future/backports", "xmlrpc", true, true);
Module['FS_createPath']("/future/backports", "html", true, true);
Module['FS_createPath']("/future/backports", "email", true, true);
Module['FS_createPath']("/future/backports/email", "mime", true, true);
Module['FS_createPath']("/future/backports", "test", true, true);
Module['FS_createPath']("/future/backports", "urllib", true, true);
Module['FS_createPath']("/future", "standard_library", true, true);
Module['FS_createPath']("/future", "tests", true, true);
Module['FS_createPath']("/future", "moves", true, true);
Module['FS_createPath']("/future/moves", "dbm", true, true);
Module['FS_createPath']("/future/moves", "http", true, true);
Module['FS_createPath']("/future/moves", "xmlrpc", true, true);
Module['FS_createPath']("/future/moves", "html", true, true);
Module['FS_createPath']("/future/moves", "test", true, true);
Module['FS_createPath']("/future/moves", "urllib", true, true);
Module['FS_createPath']("/future/moves", "tkinter", true, true);
Module['FS_createPath']("/future", "types", true, true);
Module['FS_createPath']("/future", "utils", true, true);
Module['FS_createPath']("/", "copyreg", true, true);
Module['FS_createPath']("/", "winreg", true, true);
Module['FS_createPath']("/", "typing-3.10.0.0.dist-info", true, true);
Module['FS_createPath']("/", "queue", true, true);
Module['FS_createPath']("/", "tkinter", true, true);
Module['FS_createPath']("/", "reprlib", true, true);

          /** @constructor */
          function DataRequest(start, end, audio) {
            this.start = start;
            this.end = end;
            this.audio = audio;
          }
          DataRequest.prototype = {
            requests: {},
            open: function(mode, name) {
              this.name = name;
              this.requests[name] = this;
              Module['addRunDependency']('fp ' + this.name);
            },
            send: function() {},
            onload: function() {
              var byteArray = this.byteArray.subarray(this.start, this.end);
              this.finish(byteArray);
            },
            finish: function(byteArray) {
              var that = this;
      
          Module['FS_createDataFile'](this.name, null, byteArray, true, true, true); // canOwn this data in the filesystem, it is a slide into the heap that will never change
          Module['removeRunDependency']('fp ' + that.name);
  
              this.requests[this.name] = null;
            }
          };
      
              var files = metadata['files'];
              for (var i = 0; i < files.length; ++i) {
                new DataRequest(files[i]['start'], files[i]['end'], files[i]['audio']).open('GET', files[i]['filename']);
              }
      
        
        var indexedDB;
        if (typeof window === 'object') {
          indexedDB = window.indexedDB || window.mozIndexedDB || window.webkitIndexedDB || window.msIndexedDB;
        } else if (typeof location !== 'undefined') {
          // worker
          indexedDB = self.indexedDB;
        } else {
          throw 'using IndexedDB to cache data can only be done on a web page or in a web worker';
        }
        var IDB_RO = "readonly";
        var IDB_RW = "readwrite";
        var DB_NAME = "EM_PRELOAD_CACHE";
        var DB_VERSION = 1;
        var METADATA_STORE_NAME = 'METADATA';
        var PACKAGE_STORE_NAME = 'PACKAGES';
        function openDatabase(callback, errback) {
          try {
            var openRequest = indexedDB.open(DB_NAME, DB_VERSION);
          } catch (e) {
            return errback(e);
          }
          openRequest.onupgradeneeded = function(event) {
            var db = event.target.result;

            if(db.objectStoreNames.contains(PACKAGE_STORE_NAME)) {
              db.deleteObjectStore(PACKAGE_STORE_NAME);
            }
            var packages = db.createObjectStore(PACKAGE_STORE_NAME);

            if(db.objectStoreNames.contains(METADATA_STORE_NAME)) {
              db.deleteObjectStore(METADATA_STORE_NAME);
            }
            var metadata = db.createObjectStore(METADATA_STORE_NAME);
          };
          openRequest.onsuccess = function(event) {
            var db = event.target.result;
            callback(db);
          };
          openRequest.onerror = function(error) {
            errback(error);
          };
        };

        // This is needed as chromium has a limit on per-entry files in IndexedDB
        // https://cs.chromium.org/chromium/src/content/renderer/indexed_db/webidbdatabase_impl.cc?type=cs&sq=package:chromium&g=0&l=177
        // https://cs.chromium.org/chromium/src/out/Debug/gen/third_party/blink/public/mojom/indexeddb/indexeddb.mojom.h?type=cs&sq=package:chromium&g=0&l=60
        // We set the chunk size to 64MB to stay well-below the limit
        var CHUNK_SIZE = 64 * 1024 * 1024;

        function cacheRemotePackage(
          db,
          packageName,
          packageData,
          packageMeta,
          callback,
          errback
        ) {
          var transactionPackages = db.transaction([PACKAGE_STORE_NAME], IDB_RW);
          var packages = transactionPackages.objectStore(PACKAGE_STORE_NAME);
          var chunkSliceStart = 0;
          var nextChunkSliceStart = 0;
          var chunkCount = Math.ceil(packageData.byteLength / CHUNK_SIZE);
          var finishedChunks = 0;
          for (var chunkId = 0; chunkId < chunkCount; chunkId++) {
            nextChunkSliceStart += CHUNK_SIZE;
            var putPackageRequest = packages.put(
              packageData.slice(chunkSliceStart, nextChunkSliceStart),
              'package/' + packageName + '/' + chunkId
            );
            chunkSliceStart = nextChunkSliceStart;
            putPackageRequest.onsuccess = function(event) {
              finishedChunks++;
              if (finishedChunks == chunkCount) {
                var transaction_metadata = db.transaction(
                  [METADATA_STORE_NAME],
                  IDB_RW
                );
                var metadata = transaction_metadata.objectStore(METADATA_STORE_NAME);
                var putMetadataRequest = metadata.put(
                  {
                    'uuid': packageMeta.uuid,
                    'chunkCount': chunkCount
                  },
                  'metadata/' + packageName
                );
                putMetadataRequest.onsuccess = function(event) {
                  callback(packageData);
                };
                putMetadataRequest.onerror = function(error) {
                  errback(error);
                };
              }
            };
            putPackageRequest.onerror = function(error) {
              errback(error);
            };
          }
        }

        /* Check if there's a cached package, and if so whether it's the latest available */
        function checkCachedPackage(db, packageName, callback, errback) {
          var transaction = db.transaction([METADATA_STORE_NAME], IDB_RO);
          var metadata = transaction.objectStore(METADATA_STORE_NAME);
          var getRequest = metadata.get('metadata/' + packageName);
          getRequest.onsuccess = function(event) {
            var result = event.target.result;
            if (!result) {
              return callback(false, null);
            } else {
              return callback(PACKAGE_UUID === result['uuid'], result);
            }
          };
          getRequest.onerror = function(error) {
            errback(error);
          };
        }

        function fetchCachedPackage(db, packageName, metadata, callback, errback) {
          var transaction = db.transaction([PACKAGE_STORE_NAME], IDB_RO);
          var packages = transaction.objectStore(PACKAGE_STORE_NAME);

          var chunksDone = 0;
          var totalSize = 0;
          var chunkCount = metadata['chunkCount'];
          var chunks = new Array(chunkCount);

          for (var chunkId = 0; chunkId < chunkCount; chunkId++) {
            var getRequest = packages.get('package/' + packageName + '/' + chunkId);
            getRequest.onsuccess = function(event) {
              // If there's only 1 chunk, there's nothing to concatenate it with so we can just return it now
              if (chunkCount == 1) {
                callback(event.target.result);
              } else {
                chunksDone++;
                totalSize += event.target.result.byteLength;
                chunks.push(event.target.result);
                if (chunksDone == chunkCount) {
                  if (chunksDone == 1) {
                    callback(event.target.result);
                  } else {
                    var tempTyped = new Uint8Array(totalSize);
                    var byteOffset = 0;
                    for (var chunkId in chunks) {
                      var buffer = chunks[chunkId];
                      tempTyped.set(new Uint8Array(buffer), byteOffset);
                      byteOffset += buffer.byteLength;
                      buffer = undefined;
                    }
                    chunks = undefined;
                    callback(tempTyped.buffer);
                    tempTyped = undefined;
                  }
                }
              }
            };
            getRequest.onerror = function(error) {
              errback(error);
            };
          }
        }
      
      function processPackageData(arrayBuffer) {
        assert(arrayBuffer, 'Loading data file failed.');
        assert(arrayBuffer instanceof ArrayBuffer, 'bad input to processPackageData');
        var byteArray = new Uint8Array(arrayBuffer);
        var curr;
        
          // Reuse the bytearray from the XHR as the source for file reads.
          DataRequest.prototype.byteArray = byteArray;
    
            var files = metadata['files'];
            for (var i = 0; i < files.length; ++i) {
              DataRequest.prototype.requests[files[i].filename].onload();
            }
                Module['removeRunDependency']('datafile_pyapp.data');

      };
      Module['addRunDependency']('datafile_pyapp.data');
    
      if (!Module.preloadResults) Module.preloadResults = {};
    
        function preloadFallback(error) {
          console.error(error);
          console.error('falling back to default preload behavior');
          fetchRemotePackage(REMOTE_PACKAGE_NAME, REMOTE_PACKAGE_SIZE, processPackageData, handleError);
        };

        openDatabase(
          function(db) {
            checkCachedPackage(db, PACKAGE_PATH + PACKAGE_NAME,
              function(useCached, metadata) {
                Module.preloadResults[PACKAGE_NAME] = {fromCache: useCached};
                if (useCached) {
                  fetchCachedPackage(db, PACKAGE_PATH + PACKAGE_NAME, metadata, processPackageData, preloadFallback);
                } else {
                  fetchRemotePackage(REMOTE_PACKAGE_NAME, REMOTE_PACKAGE_SIZE,
                    function(packageData) {
                      cacheRemotePackage(db, PACKAGE_PATH + PACKAGE_NAME, packageData, {uuid:PACKAGE_UUID}, processPackageData,
                        function(error) {
                          console.error(error);
                          processPackageData(packageData);
                        });
                    }
                  , preloadFallback);
                }
              }
            , preloadFallback);
          }
        , preloadFallback);

        if (Module['setStatus']) Module['setStatus']('Downloading...');
      
    }
    if (Module['calledRun']) {
      runWithFS();
    } else {
      if (!Module['preRun']) Module['preRun'] = [];
      Module["preRun"].push(runWithFS); // FS is not initialized yet, wait for it
    }
  
   }
   loadPackage({"files": [{"filename": "/web-presplash-default.jpg", "start": 0, "end": 224232, "audio": 0}, {"filename": "/six.pyo", "start": 224232, "end": 251851, "audio": 0}, {"filename": "/typing.pyo", "start": 251851, "end": 321357, "audio": 0}, {"filename": "/_dummy_thread/__init__.pyo", "start": 321357, "end": 321884, "audio": 0}, {"filename": "/http/cookies.pyo", "start": 321884, "end": 322149, "audio": 0}, {"filename": "/http/client.pyo", "start": 322149, "end": 324437, "audio": 0}, {"filename": "/http/__init__.pyo", "start": 324437, "end": 324878, "audio": 0}, {"filename": "/http/cookiejar.pyo", "start": 324878, "end": 325109, "audio": 0}, {"filename": "/http/server.pyo", "start": 325109, "end": 325587, "audio": 0}, {"filename": "/xmlrpc/client.pyo", "start": 325587, "end": 325817, "audio": 0}, {"filename": "/xmlrpc/__init__.pyo", "start": 325817, "end": 326260, "audio": 0}, {"filename": "/xmlrpc/server.pyo", "start": 326260, "end": 326490, "audio": 0}, {"filename": "/_thread/__init__.pyo", "start": 326490, "end": 327005, "audio": 0}, {"filename": "/libpasteurize/__init__.pyo", "start": 327005, "end": 327119, "audio": 0}, {"filename": "/libpasteurize/main.pyo", "start": 327119, "end": 332314, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_future_builtins.pyo", "start": 332314, "end": 333802, "audio": 0}, {"filename": "/libpasteurize/fixes/__init__.pyo", "start": 333802, "end": 334732, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_imports2.pyo", "start": 334732, "end": 344473, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_features.pyo", "start": 344473, "end": 347512, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_raise_.pyo", "start": 347512, "end": 349012, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_getcwd.pyo", "start": 349012, "end": 350098, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_newstyle.pyo", "start": 350098, "end": 351423, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_unpacking.pyo", "start": 351423, "end": 356603, "audio": 0}, {"filename": "/libpasteurize/fixes/feature_base.pyo", "start": 356603, "end": 358284, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_division.pyo", "start": 358284, "end": 359407, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_memoryview.pyo", "start": 359407, "end": 360283, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_throw.pyo", "start": 360283, "end": 361558, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_add_all_future_builtins.pyo", "start": 361558, "end": 362438, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_add_future_standard_library_import.pyo", "start": 362438, "end": 363310, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_next.pyo", "start": 363310, "end": 364948, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_imports.pyo", "start": 364948, "end": 368918, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_annotations.pyo", "start": 368918, "end": 370708, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_raise.pyo", "start": 370708, "end": 372189, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_printfunction.pyo", "start": 372189, "end": 372966, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_kwargs.pyo", "start": 372966, "end": 376670, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_fullargspec.pyo", "start": 376670, "end": 377536, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_add_all__future__imports.pyo", "start": 377536, "end": 378447, "audio": 0}, {"filename": "/libpasteurize/fixes/fix_metaclass.pyo", "start": 378447, "end": 380804, "audio": 0}, {"filename": "/six-1.12.0.dist-info/top_level.txt", "start": 380804, "end": 380808, "audio": 0}, {"filename": "/six-1.12.0.dist-info/METADATA", "start": 380808, "end": 382748, "audio": 0}, {"filename": "/six-1.12.0.dist-info/RECORD", "start": 382748, "end": 383285, "audio": 0}, {"filename": "/six-1.12.0.dist-info/INSTALLER", "start": 383285, "end": 383289, "audio": 0}, {"filename": "/six-1.12.0.dist-info/LICENSE", "start": 383289, "end": 384355, "audio": 0}, {"filename": "/six-1.12.0.dist-info/WHEEL", "start": 384355, "end": 384465, "audio": 0}, {"filename": "/socketserver/__init__.pyo", "start": 384465, "end": 384952, "audio": 0}, {"filename": "/past/__init__.pyo", "start": 384952, "end": 385242, "audio": 0}, {"filename": "/past/builtins/noniterators.pyo", "start": 385242, "end": 387365, "audio": 0}, {"filename": "/past/builtins/__init__.pyo", "start": 387365, "end": 388461, "audio": 0}, {"filename": "/past/builtins/misc.pyo", "start": 388461, "end": 390798, "audio": 0}, {"filename": "/past/types/__init__.pyo", "start": 390798, "end": 391323, "audio": 0}, {"filename": "/past/types/oldstr.pyo", "start": 391323, "end": 393889, "audio": 0}, {"filename": "/past/types/basestring.pyo", "start": 393889, "end": 394931, "audio": 0}, {"filename": "/past/types/olddict.pyo", "start": 394931, "end": 396693, "audio": 0}, {"filename": "/past/utils/__init__.pyo", "start": 396693, "end": 398172, "audio": 0}, {"filename": "/past/translation/__init__.pyo", "start": 398172, "end": 408046, "audio": 0}, {"filename": "/builtins/__init__.pyo", "start": 408046, "end": 408599, "audio": 0}, {"filename": "/libfuturize/__init__.pyo", "start": 408599, "end": 408711, "audio": 0}, {"filename": "/libfuturize/fixer_util.pyo", "start": 408711, "end": 419360, "audio": 0}, {"filename": "/libfuturize/main.pyo", "start": 419360, "end": 427452, "audio": 0}, {"filename": "/libfuturize/fixes/fix_future_builtins.pyo", "start": 427452, "end": 429034, "audio": 0}, {"filename": "/libfuturize/fixes/fix_object.pyo", "start": 429034, "end": 429772, "audio": 0}, {"filename": "/libfuturize/fixes/fix_print_with_import.pyo", "start": 429772, "end": 430548, "audio": 0}, {"filename": "/libfuturize/fixes/__init__.pyo", "start": 430548, "end": 432914, "audio": 0}, {"filename": "/libfuturize/fixes/fix_absolute_import.pyo", "start": 432914, "end": 434978, "audio": 0}, {"filename": "/libfuturize/fixes/fix_cmp.pyo", "start": 434978, "end": 435985, "audio": 0}, {"filename": "/libfuturize/fixes/fix_add__future__imports_except_unicode_literals.pyo", "start": 435985, "end": 436932, "audio": 0}, {"filename": "/libfuturize/fixes/fix_basestring.pyo", "start": 436932, "end": 437682, "audio": 0}, {"filename": "/libfuturize/fixes/fix_division.pyo", "start": 437682, "end": 437888, "audio": 0}, {"filename": "/libfuturize/fixes/fix_input.pyo", "start": 437888, "end": 438600, "audio": 0}, {"filename": "/libfuturize/fixes/fix_division_safe.pyo", "start": 438600, "end": 441448, "audio": 0}, {"filename": "/libfuturize/fixes/fix_execfile.pyo", "start": 441448, "end": 442480, "audio": 0}, {"filename": "/libfuturize/fixes/fix_unicode_literals_import.pyo", "start": 442480, "end": 443287, "audio": 0}, {"filename": "/libfuturize/fixes/fix_order___future__imports.pyo", "start": 443287, "end": 444052, "audio": 0}, {"filename": "/libfuturize/fixes/fix_bytes.pyo", "start": 444052, "end": 445006, "audio": 0}, {"filename": "/libfuturize/fixes/fix_raise.pyo", "start": 445006, "end": 447044, "audio": 0}, {"filename": "/libfuturize/fixes/fix_print.pyo", "start": 447044, "end": 449325, "audio": 0}, {"filename": "/libfuturize/fixes/fix_future_standard_library_urllib.pyo", "start": 449325, "end": 450222, "audio": 0}, {"filename": "/libfuturize/fixes/fix_UserDict.pyo", "start": 450222, "end": 452681, "audio": 0}, {"filename": "/libfuturize/fixes/fix_xrange_with_import.pyo", "start": 452681, "end": 453442, "audio": 0}, {"filename": "/libfuturize/fixes/fix_remove_old__future__imports.pyo", "start": 453442, "end": 454330, "audio": 0}, {"filename": "/libfuturize/fixes/fix_unicode_keep_u.pyo", "start": 454330, "end": 455214, "audio": 0}, {"filename": "/libfuturize/fixes/fix_oldstr_wrap.pyo", "start": 455214, "end": 456512, "audio": 0}, {"filename": "/libfuturize/fixes/fix_next_call.pyo", "start": 456512, "end": 459576, "audio": 0}, {"filename": "/libfuturize/fixes/fix_metaclass.pyo", "start": 459576, "end": 465138, "audio": 0}, {"filename": "/libfuturize/fixes/fix_future_standard_library.pyo", "start": 465138, "end": 465957, "audio": 0}, {"filename": "/bin/pasteurize", "start": 465957, "end": 466258, "audio": 0}, {"filename": "/bin/futurize", "start": 466258, "end": 466557, "audio": 0}, {"filename": "/ecdsa-0.18.0.dist-info/top_level.txt", "start": 466557, "end": 466563, "audio": 0}, {"filename": "/ecdsa-0.18.0.dist-info/METADATA", "start": 466563, "end": 496313, "audio": 0}, {"filename": "/ecdsa-0.18.0.dist-info/RECORD", "start": 496313, "end": 499670, "audio": 0}, {"filename": "/ecdsa-0.18.0.dist-info/INSTALLER", "start": 499670, "end": 499674, "audio": 0}, {"filename": "/ecdsa-0.18.0.dist-info/LICENSE", "start": 499674, "end": 500821, "audio": 0}, {"filename": "/ecdsa-0.18.0.dist-info/WHEEL", "start": 500821, "end": 500931, "audio": 0}, {"filename": "/html/__init__.pyo", "start": 500931, "end": 501415, "audio": 0}, {"filename": "/html/entities.pyo", "start": 501415, "end": 501734, "audio": 0}, {"filename": "/html/parser.pyo", "start": 501734, "end": 502150, "audio": 0}, {"filename": "/ecdsa/test_ellipticcurve.pyo", "start": 502150, "end": 509870, "audio": 0}, {"filename": "/ecdsa/eddsa.pyo", "start": 509870, "end": 517087, "audio": 0}, {"filename": "/ecdsa/test_ecdsa.pyo", "start": 517087, "end": 537071, "audio": 0}, {"filename": "/ecdsa/__init__.pyo", "start": 537071, "end": 538614, "audio": 0}, {"filename": "/ecdsa/test_malformed_sigs.pyo", "start": 538614, "end": 548340, "audio": 0}, {"filename": "/ecdsa/rfc6979.pyo", "start": 548340, "end": 550243, "audio": 0}, {"filename": "/ecdsa/curves.pyo", "start": 550243, "end": 560378, "audio": 0}, {"filename": "/ecdsa/keys.pyo", "start": 560378, "end": 579090, "audio": 0}, {"filename": "/ecdsa/numbertheory.pyo", "start": 579090, "end": 592283, "audio": 0}, {"filename": "/ecdsa/test_numbertheory.pyo", "start": 592283, "end": 607786, "audio": 0}, {"filename": "/ecdsa/ecdh.pyo", "start": 607786, "end": 612544, "audio": 0}, {"filename": "/ecdsa/test_keys.pyo", "start": 612544, "end": 645674, "audio": 0}, {"filename": "/ecdsa/_rwlock.pyo", "start": 645674, "end": 647928, "audio": 0}, {"filename": "/ecdsa/der.pyo", "start": 647928, "end": 657667, "audio": 0}, {"filename": "/ecdsa/test_der.pyo", "start": 657667, "end": 678335, "audio": 0}, {"filename": "/ecdsa/_compat.pyo", "start": 678335, "end": 683376, "audio": 0}, {"filename": "/ecdsa/errors.pyo", "start": 683376, "end": 683671, "audio": 0}, {"filename": "/ecdsa/util.pyo", "start": 683671, "end": 692747, "audio": 0}, {"filename": "/ecdsa/test_pyecdsa.pyo", "start": 692747, "end": 764514, "audio": 0}, {"filename": "/ecdsa/test_eddsa.pyo", "start": 764514, "end": 795607, "audio": 0}, {"filename": "/ecdsa/ellipticcurve.pyo", "start": 795607, "end": 829008, "audio": 0}, {"filename": "/ecdsa/test_curves.pyo", "start": 829008, "end": 843007, "audio": 0}, {"filename": "/ecdsa/test_rw_lock.pyo", "start": 843007, "end": 848544, "audio": 0}, {"filename": "/ecdsa/test_jacobi.pyo", "start": 848544, "end": 867712, "audio": 0}, {"filename": "/ecdsa/_version.pyo", "start": 867712, "end": 868183, "audio": 0}, {"filename": "/ecdsa/ecdsa.pyo", "start": 868183, "end": 884487, "audio": 0}, {"filename": "/ecdsa/test_ecdh.pyo", "start": 884487, "end": 898481, "audio": 0}, {"filename": "/ecdsa/_sha3.pyo", "start": 898481, "end": 902261, "audio": 0}, {"filename": "/ecdsa/test_sha3.pyo", "start": 902261, "end": 905499, "audio": 0}, {"filename": "/lib/python2.7/threading.pyo", "start": 905499, "end": 909937, "audio": 0}, {"filename": "/lib/python2.7/subprocess.pyo", "start": 909937, "end": 910053, "audio": 0}, {"filename": "/lib/python2.7/site-packages/pygame_sdl2/__init__.pyo", "start": 910053, "end": 914959, "audio": 0}, {"filename": "/lib/python2.7/site-packages/pygame_sdl2/compat.pyo", "start": 914959, "end": 918337, "audio": 0}, {"filename": "/lib/python2.7/site-packages/pygame_sdl2/time.pyo", "start": 918337, "end": 918526, "audio": 0}, {"filename": "/lib/python2.7/site-packages/pygame_sdl2/version.pyo", "start": 918526, "end": 919022, "audio": 0}, {"filename": "/lib/python2.7/site-packages/pygame_sdl2/sysfont.pyo", "start": 919022, "end": 939128, "audio": 0}, {"filename": "/lib/python2.7/site-packages/pygame_sdl2/sprite.pyo", "start": 939128, "end": 967349, "audio": 0}, {"filename": "/lib/python2.7/site-packages/pygame_sdl2/threads/__init__.pyo", "start": 967349, "end": 973666, "audio": 0}, {"filename": "/lib/python2.7/site-packages/pygame_sdl2/threads/Py25Queue.pyo", "start": 973666, "end": 979217, "audio": 0}, {"filename": "/_markupbase/__init__.pyo", "start": 979217, "end": 979740, "audio": 0}, {"filename": "/future-0.18.2.dist-info/top_level.txt", "start": 979740, "end": 979888, "audio": 0}, {"filename": "/future-0.18.2.dist-info/entry_points.txt", "start": 979888, "end": 979977, "audio": 0}, {"filename": "/future-0.18.2.dist-info/DESCRIPTION.rst", "start": 979977, "end": 982640, "audio": 0}, {"filename": "/future-0.18.2.dist-info/METADATA", "start": 982640, "end": 986342, "audio": 0}, {"filename": "/future-0.18.2.dist-info/metadata.json", "start": 986342, "end": 987762, "audio": 0}, {"filename": "/future-0.18.2.dist-info/RECORD", "start": 987762, "end": 1017908, "audio": 0}, {"filename": "/future-0.18.2.dist-info/LICENSE.txt", "start": 1017908, "end": 1018991, "audio": 0}, {"filename": "/future-0.18.2.dist-info/INSTALLER", "start": 1018991, "end": 1018995, "audio": 0}, {"filename": "/future-0.18.2.dist-info/WHEEL", "start": 1018995, "end": 1019088, "audio": 0}, {"filename": "/future/__init__.pyo", "start": 1019088, "end": 1019551, "audio": 0}, {"filename": "/future/builtins/__init__.pyo", "start": 1019551, "end": 1020794, "audio": 0}, {"filename": "/future/builtins/newsuper.pyo", "start": 1020794, "end": 1022597, "audio": 0}, {"filename": "/future/builtins/newnext.pyo", "start": 1022597, "end": 1023285, "audio": 0}, {"filename": "/future/builtins/newround.pyo", "start": 1023285, "end": 1025190, "audio": 0}, {"filename": "/future/builtins/iterators.pyo", "start": 1025190, "end": 1025815, "audio": 0}, {"filename": "/future/builtins/new_min_max.pyo", "start": 1025815, "end": 1027457, "audio": 0}, {"filename": "/future/builtins/misc.pyo", "start": 1027457, "end": 1029219, "audio": 0}, {"filename": "/future/builtins/disabled.pyo", "start": 1029219, "end": 1030244, "audio": 0}, {"filename": "/future/backports/_markupbase.pyo", "start": 1030244, "end": 1038856, "audio": 0}, {"filename": "/future/backports/__init__.pyo", "start": 1038856, "end": 1039501, "audio": 0}, {"filename": "/future/backports/socketserver.pyo", "start": 1039501, "end": 1053139, "audio": 0}, {"filename": "/future/backports/socket.pyo", "start": 1053139, "end": 1063758, "audio": 0}, {"filename": "/future/backports/misc.pyo", "start": 1063758, "end": 1085596, "audio": 0}, {"filename": "/future/backports/datetime.pyo", "start": 1085596, "end": 1136076, "audio": 0}, {"filename": "/future/backports/total_ordering.pyo", "start": 1136076, "end": 1138702, "audio": 0}, {"filename": "/future/backports/http/cookies.pyo", "start": 1138702, "end": 1153927, "audio": 0}, {"filename": "/future/backports/http/client.pyo", "start": 1153927, "end": 1183433, "audio": 0}, {"filename": "/future/backports/http/__init__.pyo", "start": 1183433, "end": 1183555, "audio": 0}, {"filename": "/future/backports/http/cookiejar.pyo", "start": 1183555, "end": 1231761, "audio": 0}, {"filename": "/future/backports/http/server.pyo", "start": 1231761, "end": 1261952, "audio": 0}, {"filename": "/future/backports/xmlrpc/client.pyo", "start": 1261952, "end": 1296634, "audio": 0}, {"filename": "/future/backports/xmlrpc/__init__.pyo", "start": 1296634, "end": 1296758, "audio": 0}, {"filename": "/future/backports/xmlrpc/server.pyo", "start": 1296758, "end": 1318608, "audio": 0}, {"filename": "/future/backports/html/__init__.pyo", "start": 1318608, "end": 1319258, "audio": 0}, {"filename": "/future/backports/html/entities.pyo", "start": 1319258, "end": 1384542, "audio": 0}, {"filename": "/future/backports/html/parser.pyo", "start": 1384542, "end": 1398309, "audio": 0}, {"filename": "/future/backports/email/base64mime.pyo", "start": 1398309, "end": 1400506, "audio": 0}, {"filename": "/future/backports/email/_encoded_words.pyo", "start": 1400506, "end": 1406060, "audio": 0}, {"filename": "/future/backports/email/feedparser.pyo", "start": 1406060, "end": 1417259, "audio": 0}, {"filename": "/future/backports/email/__init__.pyo", "start": 1417259, "end": 1419042, "audio": 0}, {"filename": "/future/backports/email/utils.pyo", "start": 1419042, "end": 1428629, "audio": 0}, {"filename": "/future/backports/email/_header_value_parser.pyo", "start": 1428629, "end": 1509719, "audio": 0}, {"filename": "/future/backports/email/encoders.pyo", "start": 1509719, "end": 1512129, "audio": 0}, {"filename": "/future/backports/email/headerregistry.pyo", "start": 1512129, "end": 1531310, "audio": 0}, {"filename": "/future/backports/email/errors.pyo", "start": 1531310, "end": 1536802, "audio": 0}, {"filename": "/future/backports/email/iterators.pyo", "start": 1536802, "end": 1538801, "audio": 0}, {"filename": "/future/backports/email/parser.pyo", "start": 1538801, "end": 1542497, "audio": 0}, {"filename": "/future/backports/email/_policybase.pyo", "start": 1542497, "end": 1550031, "audio": 0}, {"filename": "/future/backports/email/_parseaddr.pyo", "start": 1550031, "end": 1562263, "audio": 0}, {"filename": "/future/backports/email/message.pyo", "start": 1562263, "end": 1579605, "audio": 0}, {"filename": "/future/backports/email/policy.pyo", "start": 1579605, "end": 1583662, "audio": 0}, {"filename": "/future/backports/email/charset.pyo", "start": 1583662, "end": 1590665, "audio": 0}, {"filename": "/future/backports/email/quoprimime.pyo", "start": 1590665, "end": 1597793, "audio": 0}, {"filename": "/future/backports/email/generator.pyo", "start": 1597793, "end": 1609175, "audio": 0}, {"filename": "/future/backports/email/header.pyo", "start": 1609175, "end": 1622996, "audio": 0}, {"filename": "/future/backports/email/mime/base.pyo", "start": 1622996, "end": 1623882, "audio": 0}, {"filename": "/future/backports/email/mime/__init__.pyo", "start": 1623882, "end": 1624010, "audio": 0}, {"filename": "/future/backports/email/mime/image.pyo", "start": 1624010, "end": 1625164, "audio": 0}, {"filename": "/future/backports/email/mime/text.pyo", "start": 1625164, "end": 1626277, "audio": 0}, {"filename": "/future/backports/email/mime/audio.pyo", "start": 1626277, "end": 1627918, "audio": 0}, {"filename": "/future/backports/email/mime/application.pyo", "start": 1627918, "end": 1629036, "audio": 0}, {"filename": "/future/backports/email/mime/multipart.pyo", "start": 1629036, "end": 1630035, "audio": 0}, {"filename": "/future/backports/email/mime/nonmultipart.pyo", "start": 1630035, "end": 1630977, "audio": 0}, {"filename": "/future/backports/email/mime/message.pyo", "start": 1630977, "end": 1632083, "audio": 0}, {"filename": "/future/backports/test/keycert.passwd.pem", "start": 1632083, "end": 1633913, "audio": 0}, {"filename": "/future/backports/test/nullbytecert.pem", "start": 1633913, "end": 1639348, "audio": 0}, {"filename": "/future/backports/test/__init__.pyo", "start": 1639348, "end": 1639472, "audio": 0}, {"filename": "/future/backports/test/ssl_key.pem", "start": 1639472, "end": 1640388, "audio": 0}, {"filename": "/future/backports/test/nokia.pem", "start": 1640388, "end": 1642311, "audio": 0}, {"filename": "/future/backports/test/keycert2.pem", "start": 1642311, "end": 1644106, "audio": 0}, {"filename": "/future/backports/test/badcert.pem", "start": 1644106, "end": 1646034, "audio": 0}, {"filename": "/future/backports/test/ssl_cert.pem", "start": 1646034, "end": 1646901, "audio": 0}, {"filename": "/future/backports/test/badkey.pem", "start": 1646901, "end": 1649063, "audio": 0}, {"filename": "/future/backports/test/dh512.pem", "start": 1649063, "end": 1649465, "audio": 0}, {"filename": "/future/backports/test/support.pyo", "start": 1649465, "end": 1698702, "audio": 0}, {"filename": "/future/backports/test/ssl_servers.pyo", "start": 1698702, "end": 1706816, "audio": 0}, {"filename": "/future/backports/test/sha256.pem", "start": 1706816, "end": 1715160, "audio": 0}, {"filename": "/future/backports/test/ssl_key.passwd.pem", "start": 1715160, "end": 1716123, "audio": 0}, {"filename": "/future/backports/test/nullcert.pem", "start": 1716123, "end": 1716123, "audio": 0}, {"filename": "/future/backports/test/pystone.pyo", "start": 1716123, "end": 1722860, "audio": 0}, {"filename": "/future/backports/test/keycert.pem", "start": 1722860, "end": 1724643, "audio": 0}, {"filename": "/future/backports/test/https_svn_python_org_root.pem", "start": 1724643, "end": 1727212, "audio": 0}, {"filename": "/future/backports/urllib/__init__.pyo", "start": 1727212, "end": 1727336, "audio": 0}, {"filename": "/future/backports/urllib/response.pyo", "start": 1727336, "end": 1731381, "audio": 0}, {"filename": "/future/backports/urllib/robotparser.pyo", "start": 1731381, "end": 1737511, "audio": 0}, {"filename": "/future/backports/urllib/parse.pyo", "start": 1737511, "end": 1762876, "audio": 0}, {"filename": "/future/backports/urllib/request.pyo", "start": 1762876, "end": 1834809, "audio": 0}, {"filename": "/future/backports/urllib/error.pyo", "start": 1834809, "end": 1837262, "audio": 0}, {"filename": "/future/standard_library/__init__.pyo", "start": 1837262, "end": 1851082, "audio": 0}, {"filename": "/future/tests/base.pyo", "start": 1851082, "end": 1863991, "audio": 0}, {"filename": "/future/tests/__init__.pyo", "start": 1863991, "end": 1864104, "audio": 0}, {"filename": "/future/moves/itertools.pyo", "start": 1864104, "end": 1864447, "audio": 0}, {"filename": "/future/moves/_markupbase.pyo", "start": 1864447, "end": 1864798, "audio": 0}, {"filename": "/future/moves/__init__.pyo", "start": 1864798, "end": 1865178, "audio": 0}, {"filename": "/future/moves/copyreg.pyo", "start": 1865178, "end": 1865593, "audio": 0}, {"filename": "/future/moves/socketserver.pyo", "start": 1865593, "end": 1865948, "audio": 0}, {"filename": "/future/moves/configparser.pyo", "start": 1865948, "end": 1866264, "audio": 0}, {"filename": "/future/moves/subprocess.pyo", "start": 1866264, "end": 1866774, "audio": 0}, {"filename": "/future/moves/reprlib.pyo", "start": 1866774, "end": 1867111, "audio": 0}, {"filename": "/future/moves/collections.pyo", "start": 1867111, "end": 1867835, "audio": 0}, {"filename": "/future/moves/builtins.pyo", "start": 1867835, "end": 1868213, "audio": 0}, {"filename": "/future/moves/winreg.pyo", "start": 1868213, "end": 1868551, "audio": 0}, {"filename": "/future/moves/_thread.pyo", "start": 1868551, "end": 1868890, "audio": 0}, {"filename": "/future/moves/queue.pyo", "start": 1868890, "end": 1869224, "audio": 0}, {"filename": "/future/moves/sys.pyo", "start": 1869224, "end": 1869548, "audio": 0}, {"filename": "/future/moves/pickle.pyo", "start": 1869548, "end": 1869942, "audio": 0}, {"filename": "/future/moves/_dummy_thread.pyo", "start": 1869942, "end": 1870299, "audio": 0}, {"filename": "/future/moves/dbm/__init__.pyo", "start": 1870299, "end": 1870811, "audio": 0}, {"filename": "/future/moves/dbm/ndbm.pyo", "start": 1870811, "end": 1871149, "audio": 0}, {"filename": "/future/moves/dbm/gnu.pyo", "start": 1871149, "end": 1871486, "audio": 0}, {"filename": "/future/moves/dbm/dumb.pyo", "start": 1871486, "end": 1871828, "audio": 0}, {"filename": "/future/moves/http/cookies.pyo", "start": 1871828, "end": 1872216, "audio": 0}, {"filename": "/future/moves/http/client.pyo", "start": 1872216, "end": 1872545, "audio": 0}, {"filename": "/future/moves/http/__init__.pyo", "start": 1872545, "end": 1872769, "audio": 0}, {"filename": "/future/moves/http/cookiejar.pyo", "start": 1872769, "end": 1873125, "audio": 0}, {"filename": "/future/moves/http/server.pyo", "start": 1873125, "end": 1873725, "audio": 0}, {"filename": "/future/moves/xmlrpc/client.pyo", "start": 1873725, "end": 1874040, "audio": 0}, {"filename": "/future/moves/xmlrpc/__init__.pyo", "start": 1874040, "end": 1874160, "audio": 0}, {"filename": "/future/moves/xmlrpc/server.pyo", "start": 1874160, "end": 1874475, "audio": 0}, {"filename": "/future/moves/html/__init__.pyo", "start": 1874475, "end": 1875170, "audio": 0}, {"filename": "/future/moves/html/entities.pyo", "start": 1875170, "end": 1875529, "audio": 0}, {"filename": "/future/moves/html/parser.pyo", "start": 1875529, "end": 1875880, "audio": 0}, {"filename": "/future/moves/test/__init__.pyo", "start": 1875880, "end": 1876167, "audio": 0}, {"filename": "/future/moves/test/support.pyo", "start": 1876167, "end": 1876619, "audio": 0}, {"filename": "/future/moves/urllib/__init__.pyo", "start": 1876619, "end": 1876908, "audio": 0}, {"filename": "/future/moves/urllib/response.pyo", "start": 1876908, "end": 1877404, "audio": 0}, {"filename": "/future/moves/urllib/robotparser.pyo", "start": 1877404, "end": 1877770, "audio": 0}, {"filename": "/future/moves/urllib/parse.pyo", "start": 1877770, "end": 1878633, "audio": 0}, {"filename": "/future/moves/urllib/request.pyo", "start": 1878633, "end": 1879866, "audio": 0}, {"filename": "/future/moves/urllib/error.pyo", "start": 1879866, "end": 1880426, "audio": 0}, {"filename": "/future/moves/tkinter/commondialog.pyo", "start": 1880426, "end": 1880904, "audio": 0}, {"filename": "/future/moves/tkinter/colorchooser.pyo", "start": 1880904, "end": 1881382, "audio": 0}, {"filename": "/future/moves/tkinter/messagebox.pyo", "start": 1881382, "end": 1881852, "audio": 0}, {"filename": "/future/moves/tkinter/__init__.pyo", "start": 1881852, "end": 1882630, "audio": 0}, {"filename": "/future/moves/tkinter/scrolledtext.pyo", "start": 1882630, "end": 1883104, "audio": 0}, {"filename": "/future/moves/tkinter/constants.pyo", "start": 1883104, "end": 1883570, "audio": 0}, {"filename": "/future/moves/tkinter/dialog.pyo", "start": 1883570, "end": 1884020, "audio": 0}, {"filename": "/future/moves/tkinter/ttk.pyo", "start": 1884020, "end": 1884458, "audio": 0}, {"filename": "/future/moves/tkinter/filedialog.pyo", "start": 1884458, "end": 1884924, "audio": 0}, {"filename": "/future/moves/tkinter/tix.pyo", "start": 1884924, "end": 1885362, "audio": 0}, {"filename": "/future/moves/tkinter/font.pyo", "start": 1885362, "end": 1885808, "audio": 0}, {"filename": "/future/moves/tkinter/simpledialog.pyo", "start": 1885808, "end": 1886282, "audio": 0}, {"filename": "/future/moves/tkinter/dnd.pyo", "start": 1886282, "end": 1886724, "audio": 0}, {"filename": "/future/types/__init__.pyo", "start": 1886724, "end": 1889321, "audio": 0}, {"filename": "/future/types/newobject.pyo", "start": 1889321, "end": 1890843, "audio": 0}, {"filename": "/future/types/newrange.pyo", "start": 1890843, "end": 1896095, "audio": 0}, {"filename": "/future/types/newopen.pyo", "start": 1896095, "end": 1897477, "audio": 0}, {"filename": "/future/types/newmemoryview.pyo", "start": 1897477, "end": 1898345, "audio": 0}, {"filename": "/future/types/newlist.pyo", "start": 1898345, "end": 1900865, "audio": 0}, {"filename": "/future/types/newdict.pyo", "start": 1900865, "end": 1903207, "audio": 0}, {"filename": "/future/types/newint.pyo", "start": 1903207, "end": 1914522, "audio": 0}, {"filename": "/future/types/newbytes.pyo", "start": 1914522, "end": 1927319, "audio": 0}, {"filename": "/future/types/newstr.pyo", "start": 1927319, "end": 1938991, "audio": 0}, {"filename": "/future/utils/surrogateescape.pyo", "start": 1938991, "end": 1942856, "audio": 0}, {"filename": "/future/utils/__init__.pyo", "start": 1942856, "end": 1958163, "audio": 0}, {"filename": "/copyreg/__init__.pyo", "start": 1958163, "end": 1958641, "audio": 0}, {"filename": "/winreg/__init__.pyo", "start": 1958641, "end": 1959156, "audio": 0}, {"filename": "/typing-3.10.0.0.dist-info/top_level.txt", "start": 1959156, "end": 1959163, "audio": 0}, {"filename": "/typing-3.10.0.0.dist-info/METADATA", "start": 1959163, "end": 1961428, "audio": 0}, {"filename": "/typing-3.10.0.0.dist-info/RECORD", "start": 1961428, "end": 1962001, "audio": 0}, {"filename": "/typing-3.10.0.0.dist-info/INSTALLER", "start": 1962001, "end": 1962005, "audio": 0}, {"filename": "/typing-3.10.0.0.dist-info/LICENSE", "start": 1962005, "end": 1974760, "audio": 0}, {"filename": "/typing-3.10.0.0.dist-info/WHEEL", "start": 1974760, "end": 1974852, "audio": 0}, {"filename": "/queue/__init__.pyo", "start": 1974852, "end": 1975364, "audio": 0}, {"filename": "/tkinter/commondialog.pyo", "start": 1975364, "end": 1975829, "audio": 0}, {"filename": "/tkinter/colorchooser.pyo", "start": 1975829, "end": 1976294, "audio": 0}, {"filename": "/tkinter/messagebox.pyo", "start": 1976294, "end": 1976751, "audio": 0}, {"filename": "/tkinter/__init__.pyo", "start": 1976751, "end": 1977641, "audio": 0}, {"filename": "/tkinter/scrolledtext.pyo", "start": 1977641, "end": 1978102, "audio": 0}, {"filename": "/tkinter/constants.pyo", "start": 1978102, "end": 1978555, "audio": 0}, {"filename": "/tkinter/dialog.pyo", "start": 1978555, "end": 1978992, "audio": 0}, {"filename": "/tkinter/ttk.pyo", "start": 1978992, "end": 1979417, "audio": 0}, {"filename": "/tkinter/filedialog.pyo", "start": 1979417, "end": 1980025, "audio": 0}, {"filename": "/tkinter/tix.pyo", "start": 1980025, "end": 1980450, "audio": 0}, {"filename": "/tkinter/font.pyo", "start": 1980450, "end": 1980883, "audio": 0}, {"filename": "/tkinter/simpledialog.pyo", "start": 1980883, "end": 1981344, "audio": 0}, {"filename": "/tkinter/dnd.pyo", "start": 1981344, "end": 1981773, "audio": 0}, {"filename": "/reprlib/__init__.pyo", "start": 1981773, "end": 1982247, "audio": 0}], "remote_package_size": 1982247, "package_uuid": "34110073-9897-4c19-820e-95beb7471dd8"});
  
  })();
  