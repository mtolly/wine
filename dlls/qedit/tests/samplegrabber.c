/*
 * Sample grabber filter unit tests
 *
 * Copyright 2018 Zebediah Figura
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA
 */

#define COBJMACROS
#include "dshow.h"
#include "qedit.h"
#include "wine/strmbase.h"
#include "wine/test.h"

static IBaseFilter *create_sample_grabber(void)
{
    IBaseFilter *filter = NULL;
    HRESULT hr = CoCreateInstance(&CLSID_SampleGrabber, NULL, CLSCTX_INPROC_SERVER,
            &IID_IBaseFilter, (void **)&filter);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    return filter;
}

static ULONG get_refcount(void *iface)
{
    IUnknown *unknown = iface;
    IUnknown_AddRef(unknown);
    return IUnknown_Release(unknown);
}

static inline BOOL compare_media_types(const AM_MEDIA_TYPE *a, const AM_MEDIA_TYPE *b)
{
    return !memcmp(a, b, offsetof(AM_MEDIA_TYPE, pbFormat))
            && !memcmp(a->pbFormat, b->pbFormat, a->cbFormat);
}

#define check_interface(a, b, c) check_interface_(__LINE__, a, b, c)
static void check_interface_(unsigned int line, void *iface_ptr, REFIID iid, BOOL supported)
{
    IUnknown *iface = iface_ptr;
    HRESULT hr, expected_hr;
    ULONG ref, expect_ref;
    IUnknown *unk;

    expected_hr = supported ? S_OK : E_NOINTERFACE;

    expect_ref = get_refcount(iface);

    hr = IUnknown_QueryInterface(iface, iid, (void **)&unk);
    ok_(__FILE__, line)(hr == expected_hr, "Got hr %#x, expected %#x.\n", hr, expected_hr);
    if (SUCCEEDED(hr))
    {
        ref = get_refcount(iface);
        ok_(__FILE__, line)(ref == expect_ref + 1, "Expected %u references, got %u.\n", expect_ref + 1, ref);
        ref = get_refcount(unk);
        ok_(__FILE__, line)(ref == expect_ref + 1, "Expected %u references, got %u.\n", expect_ref + 1, ref);
        IUnknown_Release(unk);
    }
}

static void test_interfaces(void)
{
    IBaseFilter *filter = create_sample_grabber();
    IUnknown *unk;
    HRESULT hr;
    ULONG ref;
    IPin *pin;

    check_interface(filter, &IID_IBaseFilter, TRUE);
    check_interface(filter, &IID_IMediaFilter, TRUE);
    check_interface(filter, &IID_IPersist, TRUE);
    check_interface(filter, &IID_ISampleGrabber, TRUE);
    check_interface(filter, &IID_IUnknown, TRUE);

    check_interface(filter, &IID_IAMFilterMiscFlags, FALSE);
    check_interface(filter, &IID_IBasicAudio, FALSE);
    check_interface(filter, &IID_IBasicVideo, FALSE);
    check_interface(filter, &IID_IKsPropertySet, FALSE);
    check_interface(filter, &IID_IMediaPosition, FALSE);
    check_interface(filter, &IID_IMediaSeeking, FALSE);
    check_interface(filter, &IID_IMemInputPin, FALSE);
    check_interface(filter, &IID_IPersistPropertyBag, FALSE);
    check_interface(filter, &IID_IPin, FALSE);
    check_interface(filter, &IID_IQualityControl, FALSE);
    check_interface(filter, &IID_IQualProp, FALSE);
    check_interface(filter, &IID_IReferenceClock, FALSE);
    check_interface(filter, &IID_ISeekingPassThru, FALSE);
    check_interface(filter, &IID_IVideoWindow, FALSE);

    IBaseFilter_FindPin(filter, L"In", &pin);

    check_interface(pin, &IID_IMemInputPin, TRUE);
    check_interface(pin, &IID_IPin, TRUE);
    todo_wine check_interface(pin, &IID_IQualityControl, TRUE);
    check_interface(pin, &IID_IUnknown, TRUE);

    check_interface(pin, &IID_IKsPropertySet, FALSE);
    check_interface(pin, &IID_IMediaPosition, FALSE);
    check_interface(pin, &IID_IMediaSeeking, FALSE);

    IPin_Release(pin);

    IBaseFilter_FindPin(filter, L"Out", &pin);

    /* Queries for IMediaPosition or IMediaSeeking do not seem to increase the
     * reference count. */
    hr = IPin_QueryInterface(pin, &IID_IMediaPosition, (void **)&unk);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    IUnknown_Release(unk);
    hr = IPin_QueryInterface(pin, &IID_IMediaSeeking, (void **)&unk);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    IUnknown_Release(unk);
    check_interface(pin, &IID_IPin, TRUE);
    todo_wine check_interface(pin, &IID_IQualityControl, TRUE);
    check_interface(pin, &IID_IUnknown, TRUE);

    check_interface(pin, &IID_IAsyncReader, FALSE);
    check_interface(pin, &IID_IKsPropertySet, FALSE);
    check_interface(pin, &IID_IMemInputPin, FALSE);

    IPin_Release(pin);

    ref = IBaseFilter_Release(filter);
    ok(!ref, "Got unexpected refcount %d.\n", ref);
}

static void test_enum_pins(void)
{
    IBaseFilter *filter = create_sample_grabber();
    IEnumPins *enum1, *enum2;
    ULONG count, ref;
    IPin *pins[3];
    HRESULT hr;

    ref = get_refcount(filter);
    ok(ref == 1, "Got unexpected refcount %d.\n", ref);

    hr = IBaseFilter_EnumPins(filter, NULL);
    ok(hr == E_POINTER, "Got hr %#x.\n", hr);

    hr = IBaseFilter_EnumPins(filter, &enum1);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ref = get_refcount(filter);
    ok(ref == 2, "Got unexpected refcount %d.\n", ref);
    ref = get_refcount(enum1);
    ok(ref == 1, "Got unexpected refcount %d.\n", ref);

    hr = IEnumPins_Next(enum1, 1, NULL, NULL);
    ok(hr == E_POINTER, "Got hr %#x.\n", hr);

    hr = IEnumPins_Next(enum1, 1, pins, NULL);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ref = get_refcount(filter);
    ok(ref == 3, "Got unexpected refcount %d.\n", ref);
    ref = get_refcount(pins[0]);
    ok(ref == 3, "Got unexpected refcount %d.\n", ref);
    ref = get_refcount(enum1);
    ok(ref == 1, "Got unexpected refcount %d.\n", ref);
    IPin_Release(pins[0]);
    ref = get_refcount(filter);
    ok(ref == 2, "Got unexpected refcount %d.\n", ref);

    hr = IEnumPins_Next(enum1, 1, pins, NULL);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ref = get_refcount(filter);
    ok(ref == 3, "Got unexpected refcount %d.\n", ref);
    ref = get_refcount(pins[0]);
    ok(ref == 3, "Got unexpected refcount %d.\n", ref);
    ref = get_refcount(enum1);
    ok(ref == 1, "Got unexpected refcount %d.\n", ref);
    IPin_Release(pins[0]);
    ref = get_refcount(filter);
    ok(ref == 2, "Got unexpected refcount %d.\n", ref);

    hr = IEnumPins_Next(enum1, 1, pins, NULL);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);

    hr = IEnumPins_Reset(enum1);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IEnumPins_Next(enum1, 1, pins, &count);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(count == 1, "Got count %u.\n", count);
    IPin_Release(pins[0]);

    hr = IEnumPins_Next(enum1, 1, pins, &count);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(count == 1, "Got count %u.\n", count);
    IPin_Release(pins[0]);

    hr = IEnumPins_Next(enum1, 1, pins, &count);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);
    ok(!count, "Got count %u.\n", count);

    hr = IEnumPins_Reset(enum1);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IEnumPins_Next(enum1, 2, pins, NULL);
    ok(hr == E_INVALIDARG, "Got hr %#x.\n", hr);

    hr = IEnumPins_Next(enum1, 2, pins, &count);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(count == 2, "Got count %u.\n", count);
    IPin_Release(pins[0]);
    IPin_Release(pins[1]);

    hr = IEnumPins_Next(enum1, 2, pins, &count);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);
    ok(!count, "Got count %u.\n", count);

    hr = IEnumPins_Reset(enum1);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IEnumPins_Next(enum1, 3, pins, &count);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);
    ok(count == 2, "Got count %u.\n", count);
    IPin_Release(pins[0]);
    IPin_Release(pins[1]);

    hr = IEnumPins_Reset(enum1);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IEnumPins_Clone(enum1, &enum2);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IEnumPins_Skip(enum1, 3);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);

    hr = IEnumPins_Skip(enum1, 2);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IEnumPins_Skip(enum1, 1);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);

    hr = IEnumPins_Next(enum1, 1, pins, NULL);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);

    hr = IEnumPins_Next(enum2, 1, pins, NULL);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    IPin_Release(pins[0]);

    IEnumPins_Release(enum2);
    IEnumPins_Release(enum1);
    ref = IBaseFilter_Release(filter);
    ok(!ref, "Got outstanding refcount %d.\n", ref);
}

static void test_find_pin(void)
{
    IBaseFilter *filter = create_sample_grabber();
    IEnumPins *enum_pins;
    IPin *pin, *pin2;
    HRESULT hr;
    ULONG ref;

    hr = IBaseFilter_FindPin(filter, L"Input", &pin);
    ok(hr == VFW_E_NOT_FOUND, "Got hr %#x.\n", hr);
    hr = IBaseFilter_FindPin(filter, L"Output", &pin);
    ok(hr == VFW_E_NOT_FOUND, "Got hr %#x.\n", hr);

    hr = IBaseFilter_EnumPins(filter, &enum_pins);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IBaseFilter_FindPin(filter, L"In", &pin);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IEnumPins_Next(enum_pins, 1, &pin2, NULL);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(pin2 == pin, "Expected pin %p, got %p.\n", pin, pin2);
    IPin_Release(pin2);
    IPin_Release(pin);

    hr = IBaseFilter_FindPin(filter, L"Out", &pin);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IEnumPins_Next(enum_pins, 1, &pin2, NULL);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(pin2 == pin, "Expected pin %p, got %p.\n", pin, pin2);
    IPin_Release(pin2);
    IPin_Release(pin);

    IEnumPins_Release(enum_pins);
    ref = IBaseFilter_Release(filter);
    ok(!ref, "Got outstanding refcount %d.\n", ref);
}

static void test_pin_info(void)
{
    IBaseFilter *filter = create_sample_grabber();
    PIN_DIRECTION dir;
    PIN_INFO info;
    ULONG count;
    HRESULT hr;
    WCHAR *id;
    ULONG ref;
    IPin *pin;

    hr = IBaseFilter_FindPin(filter, L"In", &pin);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IPin_QueryPinInfo(pin, &info);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(info.pFilter == filter, "Expected filter %p, got %p.\n", filter, info.pFilter);
    ok(info.dir == PINDIR_INPUT, "Got direction %d.\n", info.dir);
    ok(!wcscmp(info.achName, L"Input"), "Got name %s.\n", wine_dbgstr_w(info.achName));
    IBaseFilter_Release(info.pFilter);

    hr = IPin_QueryDirection(pin, &dir);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(dir == PINDIR_INPUT, "Got direction %d.\n", dir);

    hr = IPin_QueryId(pin, &id);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(!wcscmp(id, L"In"), "Got id %s.\n", wine_dbgstr_w(id));
    CoTaskMemFree(id);

    hr = IPin_QueryInternalConnections(pin, NULL, &count);
    ok(hr == E_NOTIMPL, "Got hr %#x.\n", hr);

    IPin_Release(pin);

    hr = IBaseFilter_FindPin(filter, L"Out", &pin);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IPin_QueryPinInfo(pin, &info);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(info.pFilter == filter, "Expected filter %p, got %p.\n", filter, info.pFilter);
    ok(info.dir == PINDIR_OUTPUT, "Got direction %d.\n", info.dir);
    ok(!wcscmp(info.achName, L"Output"), "Got name %s.\n", wine_dbgstr_w(info.achName));
    IBaseFilter_Release(info.pFilter);

    hr = IPin_QueryDirection(pin, &dir);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(dir == PINDIR_OUTPUT, "Got direction %d.\n", dir);

    hr = IPin_QueryId(pin, &id);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(!wcscmp(id, L"Out"), "Got id %s.\n", wine_dbgstr_w(id));
    CoTaskMemFree(id);

    hr = IPin_QueryInternalConnections(pin, NULL, &count);
    ok(hr == E_NOTIMPL, "Got hr %#x.\n", hr);

    IPin_Release(pin);

    ref = IBaseFilter_Release(filter);
    ok(!ref, "Got outstanding refcount %d.\n", ref);
}

static const GUID test_iid = {0x33333333};
static LONG outer_ref = 1;

static HRESULT WINAPI outer_QueryInterface(IUnknown *iface, REFIID iid, void **out)
{
    if (IsEqualGUID(iid, &IID_IUnknown)
            || IsEqualGUID(iid, &IID_IBaseFilter)
            || IsEqualGUID(iid, &test_iid))
    {
        *out = (IUnknown *)0xdeadbeef;
        return S_OK;
    }
    ok(0, "unexpected call %s\n", wine_dbgstr_guid(iid));
    return E_NOINTERFACE;
}

static ULONG WINAPI outer_AddRef(IUnknown *iface)
{
    return InterlockedIncrement(&outer_ref);
}

static ULONG WINAPI outer_Release(IUnknown *iface)
{
    return InterlockedDecrement(&outer_ref);
}

static const IUnknownVtbl outer_vtbl =
{
    outer_QueryInterface,
    outer_AddRef,
    outer_Release,
};

static IUnknown test_outer = {&outer_vtbl};

static void test_aggregation(void)
{
    IBaseFilter *filter, *filter2;
    IUnknown *unk, *unk2;
    HRESULT hr;
    ULONG ref;

    filter = (IBaseFilter *)0xdeadbeef;
    hr = CoCreateInstance(&CLSID_SampleGrabber, &test_outer, CLSCTX_INPROC_SERVER,
            &IID_IBaseFilter, (void **)&filter);
    ok(hr == E_NOINTERFACE, "Got hr %#x.\n", hr);
    ok(!filter, "Got interface %p.\n", filter);

    hr = CoCreateInstance(&CLSID_SampleGrabber, &test_outer, CLSCTX_INPROC_SERVER,
            &IID_IUnknown, (void **)&unk);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(outer_ref == 1, "Got unexpected refcount %d.\n", outer_ref);
    ok(unk != &test_outer, "Returned IUnknown should not be outer IUnknown.\n");
    ref = get_refcount(unk);
    ok(ref == 1, "Got unexpected refcount %d.\n", ref);

    ref = IUnknown_AddRef(unk);
    ok(ref == 2, "Got unexpected refcount %d.\n", ref);
    ok(outer_ref == 1, "Got unexpected refcount %d.\n", outer_ref);

    ref = IUnknown_Release(unk);
    ok(ref == 1, "Got unexpected refcount %d.\n", ref);
    ok(outer_ref == 1, "Got unexpected refcount %d.\n", outer_ref);

    hr = IUnknown_QueryInterface(unk, &IID_IUnknown, (void **)&unk2);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(unk2 == unk, "Got unexpected IUnknown %p.\n", unk2);
    IUnknown_Release(unk2);

    hr = IUnknown_QueryInterface(unk, &IID_IBaseFilter, (void **)&filter);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IBaseFilter_QueryInterface(filter, &IID_IUnknown, (void **)&unk2);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(unk2 == (IUnknown *)0xdeadbeef, "Got unexpected IUnknown %p.\n", unk2);

    hr = IBaseFilter_QueryInterface(filter, &IID_IBaseFilter, (void **)&filter2);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(filter2 == (IBaseFilter *)0xdeadbeef, "Got unexpected IBaseFilter %p.\n", filter2);

    hr = IUnknown_QueryInterface(unk, &test_iid, (void **)&unk2);
    ok(hr == E_NOINTERFACE, "Got hr %#x.\n", hr);
    ok(!unk2, "Got unexpected IUnknown %p.\n", unk2);

    hr = IBaseFilter_QueryInterface(filter, &test_iid, (void **)&unk2);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(unk2 == (IUnknown *)0xdeadbeef, "Got unexpected IUnknown %p.\n", unk2);

    IBaseFilter_Release(filter);
    ref = IUnknown_Release(unk);
    ok(!ref, "Got unexpected refcount %d.\n", ref);
    ok(outer_ref == 1, "Got unexpected refcount %d.\n", outer_ref);
}

static void test_media_types(void)
{
    BYTE format = 1;
    AM_MEDIA_TYPE mt =
    {
        .majortype = {0x111},
        .subtype = {0x222},
        .formattype = {0x333},
    };
    AM_MEDIA_TYPE match_mt =
    {
        .subtype = {0x123},
        .bFixedSizeSamples = TRUE,
        .bTemporalCompression = TRUE,
        .lSampleSize = 456,
        .formattype = {0x789},
        .cbFormat = sizeof(format),
        .pbFormat = &format,
    };
    IBaseFilter *filter = create_sample_grabber();
    IEnumMediaTypes *enummt;
    ISampleGrabber *grabber;
    IPin *sink, *source;
    HRESULT hr;
    ULONG ref;

    IBaseFilter_QueryInterface(filter, &IID_ISampleGrabber, (void **)&grabber);
    IBaseFilter_FindPin(filter, L"In", &sink);
    IBaseFilter_FindPin(filter, L"Out", &source);

    hr = IPin_EnumMediaTypes(sink, &enummt);
    ok(hr == VFW_E_NOT_CONNECTED, "Got hr %#x.\n", hr);

    hr = IPin_EnumMediaTypes(source, &enummt);
    ok(hr == VFW_E_NOT_CONNECTED, "Got hr %#x.\n", hr);

    hr = IPin_QueryAccept(sink, &mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IPin_QueryAccept(source, &mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = ISampleGrabber_SetMediaType(grabber, &match_mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IPin_EnumMediaTypes(sink, &enummt);
    ok(hr == VFW_E_NOT_CONNECTED, "Got hr %#x.\n", hr);

    hr = IPin_EnumMediaTypes(source, &enummt);
    ok(hr == VFW_E_NOT_CONNECTED, "Got hr %#x.\n", hr);

    hr = IPin_QueryAccept(sink, &mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IPin_QueryAccept(source, &mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    match_mt.majortype = MEDIATYPE_Video;
    match_mt.subtype = GUID_NULL;
    hr = ISampleGrabber_SetMediaType(grabber, &match_mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IPin_QueryAccept(sink, &mt);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);
    hr = IPin_QueryAccept(source, &mt);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);

    mt.majortype = GUID_NULL;
    hr = IPin_QueryAccept(sink, &mt);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);
    hr = IPin_QueryAccept(source, &mt);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);
    mt.majortype = match_mt.majortype;
    hr = IPin_QueryAccept(sink, &mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IPin_QueryAccept(source, &mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    match_mt.subtype = MEDIASUBTYPE_RGB8;
    match_mt.formattype = GUID_NULL;
    hr = ISampleGrabber_SetMediaType(grabber, &match_mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IPin_QueryAccept(sink, &mt);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);
    hr = IPin_QueryAccept(source, &mt);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);

    mt.subtype = GUID_NULL;
    hr = IPin_QueryAccept(sink, &mt);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);
    hr = IPin_QueryAccept(source, &mt);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);
    mt.subtype = match_mt.subtype;
    hr = IPin_QueryAccept(sink, &mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IPin_QueryAccept(source, &mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    match_mt.formattype = FORMAT_None;
    hr = ISampleGrabber_SetMediaType(grabber, &match_mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IPin_QueryAccept(sink, &mt);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);
    hr = IPin_QueryAccept(source, &mt);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);

    mt.formattype = GUID_NULL;
    hr = IPin_QueryAccept(sink, &mt);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);
    hr = IPin_QueryAccept(source, &mt);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);
    mt.formattype = match_mt.formattype;
    hr = IPin_QueryAccept(sink, &mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IPin_QueryAccept(source, &mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    IPin_Release(sink);
    IPin_Release(source);
    ISampleGrabber_Release(grabber);
    ref = IBaseFilter_Release(filter);
    ok(!ref, "Got outstanding refcount %d.\n", ref);
}

struct testfilter
{
    struct strmbase_filter filter;
    struct strmbase_source source;
    struct strmbase_sink sink;
    const AM_MEDIA_TYPE *sink_mt;
    AM_MEDIA_TYPE source_mt;
    unsigned int got_sample, got_new_segment, got_eos, got_begin_flush, got_end_flush;
};

static inline struct testfilter *impl_from_strmbase_filter(struct strmbase_filter *iface)
{
    return CONTAINING_RECORD(iface, struct testfilter, filter);
}

static struct strmbase_pin *testfilter_get_pin(struct strmbase_filter *iface, unsigned int index)
{
    struct testfilter *filter = impl_from_strmbase_filter(iface);
    if (!index)
        return &filter->source.pin;
    else if (index == 1)
        return &filter->sink.pin;
    return NULL;
}

static void testfilter_destroy(struct strmbase_filter *iface)
{
    struct testfilter *filter = impl_from_strmbase_filter(iface);
    strmbase_source_cleanup(&filter->source);
    strmbase_sink_cleanup(&filter->sink);
    strmbase_filter_cleanup(&filter->filter);
}

static const struct strmbase_filter_ops testfilter_ops =
{
    .filter_get_pin = testfilter_get_pin,
    .filter_destroy = testfilter_destroy,
};

static HRESULT testsource_query_accept(struct strmbase_pin *iface, const AM_MEDIA_TYPE *mt)
{
    return mt->bTemporalCompression ? S_OK : S_FALSE;
}

static HRESULT testsource_get_media_type(struct strmbase_pin *iface, unsigned int index, AM_MEDIA_TYPE *mt)
{
    struct testfilter *filter = impl_from_strmbase_filter(iface->filter);
    if (!index)
    {
        CopyMediaType(mt, &filter->source_mt);
        return S_OK;
    }
    return VFW_S_NO_MORE_ITEMS;
}

static void test_sink_allocator(IPin *pin)
{
    ALLOCATOR_PROPERTIES req_props = {1, 256, 1, 0}, ret_props;
    IMemAllocator *req_allocator, *ret_allocator;
    IMemInputPin *input;
    HRESULT hr;

    IPin_QueryInterface(pin, &IID_IMemInputPin, (void **)&input);

    hr = IMemInputPin_NotifyAllocator(input, NULL, TRUE);
    todo_wine ok(hr == E_POINTER, "Got hr %#x.\n", hr);

    hr = IMemInputPin_GetAllocatorRequirements(input, &ret_props);
    ok(hr == E_NOTIMPL, "Got hr %#x.\n", hr);

    hr = IMemInputPin_GetAllocator(input, &ret_allocator);
    todo_wine ok(hr == S_OK, "Got hr %#x.\n", hr);

    if (hr == S_OK)
    {
        hr = IMemInputPin_NotifyAllocator(input, ret_allocator, TRUE);
        ok(hr == S_OK, "Got hr %#x.\n", hr);
        IMemAllocator_Release(ret_allocator);
    }

    CoCreateInstance(&CLSID_MemoryAllocator, NULL, CLSCTX_INPROC_SERVER,
            &IID_IMemAllocator, (void **)&req_allocator);

    hr = IMemInputPin_NotifyAllocator(input, req_allocator, TRUE);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IMemInputPin_GetAllocator(input, &ret_allocator);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(ret_allocator == req_allocator, "Allocators didn't match.\n");
    IMemAllocator_Release(ret_allocator);

    hr = IMemAllocator_SetProperties(req_allocator, &req_props, &ret_props);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    IMemAllocator_Release(req_allocator);
    IMemInputPin_Release(input);
}

static HRESULT WINAPI testsource_AttemptConnection(struct strmbase_source *iface,
        IPin *peer, const AM_MEDIA_TYPE *mt)
{
    HRESULT hr;

    iface->pin.peer = peer;
    IPin_AddRef(peer);
    CopyMediaType(&iface->pin.mt, mt);

    if (FAILED(hr = IPin_ReceiveConnection(peer, &iface->pin.IPin_iface, mt)))
    {
        ok(hr == VFW_E_TYPE_NOT_ACCEPTED, "Got hr %#x.\n", hr);
        IPin_Release(peer);
        iface->pin.peer = NULL;
        FreeMediaType(&iface->pin.mt);
    }

    test_sink_allocator(peer);

    return hr;
}

static const struct strmbase_source_ops testsource_ops =
{
    .base.pin_query_accept = testsource_query_accept,
    .base.pin_get_media_type = testsource_get_media_type,
    .pfnAttemptConnection = testsource_AttemptConnection,
};

static HRESULT testsink_query_interface(struct strmbase_pin *iface, REFIID iid, void **out)
{
    struct testfilter *filter = impl_from_strmbase_filter(iface->filter);

    if (IsEqualGUID(iid, &IID_IMemInputPin))
        *out = &filter->sink.IMemInputPin_iface;
    else
        return E_NOINTERFACE;

    IUnknown_AddRef((IUnknown *)*out);
    return S_OK;
}

static HRESULT testsink_get_media_type(struct strmbase_pin *iface, unsigned int index, AM_MEDIA_TYPE *mt)
{
    struct testfilter *filter = impl_from_strmbase_filter(iface->filter);
    if (!index && filter->sink_mt)
    {
        CopyMediaType(mt, filter->sink_mt);
        return S_OK;
    }
    return VFW_S_NO_MORE_ITEMS;
}

static HRESULT testsink_connect(struct strmbase_sink *iface, IPin *peer, const AM_MEDIA_TYPE *mt)
{
    struct testfilter *filter = impl_from_strmbase_filter(iface->pin.filter);
    if (filter->sink_mt && !IsEqualGUID(&mt->majortype, &filter->sink_mt->majortype))
        return VFW_E_TYPE_NOT_ACCEPTED;
    return S_OK;
}

static HRESULT WINAPI testsink_Receive(struct strmbase_sink *iface, IMediaSample *sample)
{
    struct testfilter *filter = impl_from_strmbase_filter(iface->pin.filter);
    REFERENCE_TIME start, stop;
    BYTE *data, expect[200];
    LONG size, i;
    HRESULT hr;

    size = IMediaSample_GetSize(sample);
    ok(size == 256, "Got size %u.\n", size);
    size = IMediaSample_GetActualDataLength(sample);
    ok(size == 200, "Got valid size %u.\n", size);

    hr = IMediaSample_GetPointer(sample, &data);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    for (i = 0; i < size; ++i)
        expect[i] = i;
    ok(!memcmp(data, expect, size), "Data didn't match.\n");

    hr = IMediaSample_GetTime(sample, &start, &stop);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(start == 30000, "Got start time %s.\n", wine_dbgstr_longlong(start));
    ok(stop == 40000, "Got stop time %s.\n", wine_dbgstr_longlong(stop));

    hr = IMediaSample_GetMediaTime(sample, &start, &stop);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(start == 10000, "Got start time %s.\n", wine_dbgstr_longlong(start));
    ok(stop == 20000, "Got stop time %s.\n", wine_dbgstr_longlong(stop));

    hr = IMediaSample_IsDiscontinuity(sample);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IMediaSample_IsPreroll(sample);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);
    hr = IMediaSample_IsSyncPoint(sample);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    ++filter->got_sample;

    return S_OK;
}

static HRESULT testsink_new_segment(struct strmbase_sink *iface,
        REFERENCE_TIME start, REFERENCE_TIME stop, double rate)
{
    struct testfilter *filter = impl_from_strmbase_filter(iface->pin.filter);
    ++filter->got_new_segment;
    ok(start == 10000, "Got start %s.\n", wine_dbgstr_longlong(start));
    ok(stop == 20000, "Got stop %s.\n", wine_dbgstr_longlong(stop));
    ok(rate == 1.0, "Got rate %.16e.\n", rate);
    return S_OK;
}

static HRESULT testsink_eos(struct strmbase_sink *iface)
{
    struct testfilter *filter = impl_from_strmbase_filter(iface->pin.filter);
    ++filter->got_eos;
    return S_OK;
}

static HRESULT testsink_begin_flush(struct strmbase_sink *iface)
{
    struct testfilter *filter = impl_from_strmbase_filter(iface->pin.filter);
    ++filter->got_begin_flush;
    return S_OK;
}

static HRESULT testsink_end_flush(struct strmbase_sink *iface)
{
    struct testfilter *filter = impl_from_strmbase_filter(iface->pin.filter);
    ++filter->got_end_flush;
    return S_OK;
}

static const struct strmbase_sink_ops testsink_ops =
{
    .base.pin_query_interface = testsink_query_interface,
    .base.pin_get_media_type = testsink_get_media_type,
    .sink_connect = testsink_connect,
    .pfnReceive = testsink_Receive,
    .sink_new_segment = testsink_new_segment,
    .sink_eos = testsink_eos,
    .sink_begin_flush = testsink_begin_flush,
    .sink_end_flush = testsink_end_flush,
};

static void testfilter_init(struct testfilter *filter)
{
    static const GUID clsid = {0xabacab};
    memset(filter, 0, sizeof(*filter));
    strmbase_filter_init(&filter->filter, NULL, &clsid, &testfilter_ops);
    strmbase_source_init(&filter->source, &filter->filter, L"source", &testsource_ops);
    strmbase_sink_init(&filter->sink, &filter->filter, L"sink", &testsink_ops, NULL);
}

static void test_sample_processing(IMediaControl *control, IMemInputPin *input, struct testfilter *sink)
{
    REFERENCE_TIME start, stop;
    IMemAllocator *allocator;
    IMediaSample *sample;
    LONG size, i;
    HRESULT hr;
    BYTE *data;

    hr = IMemInputPin_ReceiveCanBlock(input);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IMemInputPin_GetAllocator(input, &allocator);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IMemAllocator_GetBuffer(allocator, &sample, NULL, NULL, 0);
    ok(hr == VFW_E_NOT_COMMITTED, "Got hr %#x.\n", hr);

    hr = IMediaControl_Pause(control);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IMemAllocator_GetBuffer(allocator, &sample, NULL, NULL, 0);
    todo_wine ok(hr == S_OK, "Got hr %#x.\n", hr);
    if (hr != S_OK)
    {
        IMemAllocator_Commit(allocator);
        hr = IMemAllocator_GetBuffer(allocator, &sample, NULL, NULL, 0);
        ok(hr == S_OK, "Got hr %#x.\n", hr);
    }

    hr = IMediaSample_GetPointer(sample, &data);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    size = IMediaSample_GetSize(sample);
    ok(size == 256, "Got size %d.\n", size);
    for (i = 0; i < 200; ++i)
        data[i] = i;
    hr = IMediaSample_SetActualDataLength(sample, 200);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    start = 10000;
    stop = 20000;
    hr = IMediaSample_SetMediaTime(sample, &start, &stop);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    start = 30000;
    stop = 40000;
    hr = IMediaSample_SetTime(sample, &start, &stop);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IMediaSample_SetDiscontinuity(sample, TRUE);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IMediaSample_SetSyncPoint(sample, TRUE);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IMemInputPin_Receive(input, sample);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(sink->got_sample == 1, "Got %u calls to Receive().\n", sink->got_sample);
    sink->got_sample = 0;

    hr = IMediaControl_Stop(control);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IMemInputPin_Receive(input, sample);
    todo_wine ok(hr == VFW_E_WRONG_STATE, "Got hr %#x.\n", hr);

    IMediaSample_Release(sample);
    IMemAllocator_Release(allocator);
}

static void test_streaming_events(IMediaControl *control, IPin *sink,
        IMemInputPin *input, struct testfilter *testsink)
{
    REFERENCE_TIME start, stop;
    IMemAllocator *allocator;
    IMediaSample *sample;
    HRESULT hr;
    BYTE *data;
    LONG i;

    hr = IMediaControl_Pause(control);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IMemInputPin_GetAllocator(input, &allocator);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IMemAllocator_GetBuffer(allocator, &sample, NULL, NULL, 0);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IMediaSample_GetPointer(sample, &data);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    for (i = 0; i < 200; ++i)
        data[i] = i;
    hr = IMediaSample_SetActualDataLength(sample, 200);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    start = 10000;
    stop = 20000;
    hr = IMediaSample_SetMediaTime(sample, &start, &stop);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    start = 30000;
    stop = 40000;
    hr = IMediaSample_SetTime(sample, &start, &stop);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IMediaSample_SetDiscontinuity(sample, TRUE);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IMediaSample_SetSyncPoint(sample, TRUE);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    ok(!testsink->got_new_segment, "Got %u calls to IPin::NewSegment().\n", testsink->got_new_segment);
    hr = IPin_NewSegment(sink, 10000, 20000, 1.0);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(testsink->got_new_segment == 1, "Got %u calls to IPin::NewSegment().\n", testsink->got_new_segment);

    ok(!testsink->got_eos, "Got %u calls to IPin::EndOfStream().\n", testsink->got_eos);
    hr = IPin_EndOfStream(sink);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    todo_wine ok(!testsink->got_sample, "Got %u calls to Receive().\n", testsink->got_sample);
    ok(testsink->got_eos == 1, "Got %u calls to IPin::EndOfStream().\n", testsink->got_eos);
    testsink->got_eos = 0;

    hr = IPin_EndOfStream(sink);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(testsink->got_eos == 1, "Got %u calls to IPin::EndOfStream().\n", testsink->got_eos);
    testsink->got_eos = 0;

    hr = IMemInputPin_Receive(input, sample);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    todo_wine ok(testsink->got_sample == 1, "Got %u calls to Receive().\n", testsink->got_sample);
    testsink->got_sample = 0;

    ok(!testsink->got_begin_flush, "Got %u calls to IPin::BeginFlush().\n", testsink->got_begin_flush);
    hr = IPin_BeginFlush(sink);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(testsink->got_begin_flush == 1, "Got %u calls to IPin::BeginFlush().\n", testsink->got_begin_flush);

    hr = IMemInputPin_Receive(input, sample);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(testsink->got_sample == 1, "Got %u calls to Receive().\n", testsink->got_sample);
    testsink->got_sample = 0;

    hr = IPin_EndOfStream(sink);
    todo_wine ok(hr == S_OK, "Got hr %#x.\n", hr);
    todo_wine ok(testsink->got_eos == 1, "Got %u calls to IPin::EndOfStream().\n", testsink->got_eos);
    testsink->got_eos = 0;

    ok(!testsink->got_end_flush, "Got %u calls to IPin::EndFlush().\n", testsink->got_end_flush);
    hr = IPin_EndFlush(sink);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(testsink->got_end_flush == 1, "Got %u calls to IPin::EndFlush().\n", testsink->got_end_flush);

    hr = IMemInputPin_Receive(input, sample);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(testsink->got_sample == 1, "Got %u calls to Receive().\n", testsink->got_sample);
    testsink->got_sample = 0;

    hr = IMediaControl_Stop(control);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    IMediaSample_Release(sample);
    IMemAllocator_Release(allocator);
}

static void test_connect_pin(void)
{
    AM_MEDIA_TYPE req_mt =
    {
        .majortype = MEDIATYPE_Stream,
        .subtype = MEDIASUBTYPE_Avi,
        .formattype = FORMAT_None,
    };
    IBaseFilter *filter = create_sample_grabber();
    struct testfilter testsource, testsink;
    IPin *sink, *source, *peer;
    IEnumMediaTypes *enummt;
    ISampleGrabber *grabber;
    IMediaControl *control;
    AM_MEDIA_TYPE mt, *pmt;
    IFilterGraph2 *graph;
    IMemInputPin *input;
    HRESULT hr;
    ULONG ref;

    testfilter_init(&testsource);
    testfilter_init(&testsink);
    CoCreateInstance(&CLSID_FilterGraph, NULL, CLSCTX_INPROC_SERVER,
            &IID_IFilterGraph2, (void **)&graph);
    IFilterGraph2_AddFilter(graph, &testsource.filter.IBaseFilter_iface, L"source");
    IFilterGraph2_AddFilter(graph, &testsink.filter.IBaseFilter_iface, L"sink");
    IFilterGraph2_AddFilter(graph, filter, L"sample grabber");
    IFilterGraph2_QueryInterface(graph, &IID_IMediaControl, (void **)&control);
    IBaseFilter_FindPin(filter, L"In", &sink);
    IPin_QueryInterface(sink, &IID_IMemInputPin, (void **)&input);
    IBaseFilter_FindPin(filter, L"Out", &source);
    IBaseFilter_QueryInterface(filter, &IID_ISampleGrabber, (void **)&grabber);

    testsource.source_mt.majortype = MEDIATYPE_Video;
    testsource.source_mt.subtype = MEDIASUBTYPE_RGB8;
    testsource.source_mt.formattype = FORMAT_VideoInfo;

    hr = ISampleGrabber_GetConnectedMediaType(grabber, &mt);
    ok(hr == VFW_E_NOT_CONNECTED, "Got hr %#x.\n", hr);

    /* Test sink connection. */

    peer = (IPin *)0xdeadbeef;
    hr = IPin_ConnectedTo(sink, &peer);
    ok(hr == VFW_E_NOT_CONNECTED, "Got hr %#x.\n", hr);
    ok(!peer, "Got peer %p.\n", peer);

    hr = IPin_ConnectionMediaType(sink, &mt);
    ok(hr == VFW_E_NOT_CONNECTED, "Got hr %#x.\n", hr);

    hr = IMediaControl_Pause(control);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IFilterGraph2_ConnectDirect(graph, &testsource.source.pin.IPin_iface, sink, &req_mt);
    ok(hr == VFW_E_NOT_STOPPED, "Got hr %#x.\n", hr);
    hr = IMediaControl_Stop(control);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IFilterGraph2_ConnectDirect(graph, &testsource.source.pin.IPin_iface, sink, &req_mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IPin_ConnectedTo(sink, &peer);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(peer == &testsource.source.pin.IPin_iface, "Got peer %p.\n", peer);
    IPin_Release(peer);

    hr = IPin_ConnectionMediaType(sink, &mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(compare_media_types(&mt, &req_mt), "Media types didn't match.\n");

    hr = IMediaControl_Pause(control);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IFilterGraph2_Disconnect(graph, sink);
    ok(hr == VFW_E_NOT_STOPPED, "Got hr %#x.\n", hr);
    hr = IMediaControl_Stop(control);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = ISampleGrabber_GetConnectedMediaType(grabber, NULL);
    ok(hr == E_POINTER, "Got hr %#x.\n", hr);

    hr = ISampleGrabber_GetConnectedMediaType(grabber, &mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(compare_media_types(&mt, &req_mt), "Media types didn't match.\n");

    hr = IPin_EnumMediaTypes(sink, &enummt);
    ok(hr == VFW_E_NOT_CONNECTED, "Got hr %#x.\n", hr);
    hr = IPin_EnumMediaTypes(source, &enummt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IEnumMediaTypes_Next(enummt, 1, &pmt, NULL);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(compare_media_types(pmt, &testsource.source_mt), "Media types didn't match.\n");
    IEnumMediaTypes_Release(enummt);

    req_mt.majortype = MEDIATYPE_Video;
    req_mt.subtype = MEDIASUBTYPE_RGB8;
    req_mt.formattype = FORMAT_VideoInfo;
    hr = IPin_QueryAccept(sink, &req_mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IPin_QueryAccept(source, &req_mt);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);
    req_mt.bTemporalCompression = TRUE;
    hr = IPin_QueryAccept(source, &req_mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    memset(&mt, 0, sizeof(AM_MEDIA_TYPE));
    mt.majortype = MEDIATYPE_Midi;
    hr = ISampleGrabber_SetMediaType(grabber, &mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IPin_QueryAccept(source, &req_mt);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);

    req_mt.majortype = MEDIATYPE_Midi;
    req_mt.bTemporalCompression = FALSE;
    hr = IPin_QueryAccept(source, &req_mt);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);

    req_mt.bTemporalCompression = TRUE;
    hr = IPin_QueryAccept(source, &req_mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    memset(&mt, 0, sizeof(AM_MEDIA_TYPE));
    hr = ISampleGrabber_SetMediaType(grabber, &mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    /* Test source connection. */

    peer = (IPin *)0xdeadbeef;
    hr = IPin_ConnectedTo(source, &peer);
    ok(hr == VFW_E_NOT_CONNECTED, "Got hr %#x.\n", hr);
    ok(!peer, "Got peer %p.\n", peer);

    hr = IPin_ConnectionMediaType(source, &mt);
    ok(hr == VFW_E_NOT_CONNECTED, "Got hr %#x.\n", hr);

    /* Exact connection. */

    hr = IMediaControl_Pause(control);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IFilterGraph2_ConnectDirect(graph, source, &testsink.sink.pin.IPin_iface, &req_mt);
    ok(hr == VFW_E_NOT_STOPPED, "Got hr %#x.\n", hr);
    hr = IMediaControl_Stop(control);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    req_mt.bTemporalCompression = FALSE;
    hr = IFilterGraph2_ConnectDirect(graph, source, &testsink.sink.pin.IPin_iface, &req_mt);
    ok(hr == VFW_E_TYPE_NOT_ACCEPTED, "Got hr %#x.\n", hr);

    req_mt.bTemporalCompression = TRUE;
    hr = IFilterGraph2_ConnectDirect(graph, source, &testsink.sink.pin.IPin_iface, &req_mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IPin_ConnectedTo(source, &peer);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(peer == &testsink.sink.pin.IPin_iface, "Got peer %p.\n", peer);
    IPin_Release(peer);

    hr = IPin_ConnectionMediaType(source, &mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(compare_media_types(&mt, &req_mt), "Media types didn't match.\n");
    ok(compare_media_types(&testsink.sink.pin.mt, &req_mt), "Media types didn't match.\n");
    ok(compare_media_types(&testsource.source.pin.mt, &testsink.sink.pin.mt), "Media types didn't match.\n");

    test_sample_processing(control, input, &testsink);
    test_streaming_events(control, sink, input, &testsink);

    hr = IMediaControl_Pause(control);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IFilterGraph2_Disconnect(graph, source);
    ok(hr == VFW_E_NOT_STOPPED, "Got hr %#x.\n", hr);
    hr = IMediaControl_Stop(control);
    ok(hr == S_OK, "Got hr %#x.\n", hr);

    hr = IFilterGraph2_Disconnect(graph, source);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IFilterGraph2_Disconnect(graph, source);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);
    ok(testsink.sink.pin.peer == source, "Got peer %p.\n", testsink.sink.pin.peer);
    IFilterGraph2_Disconnect(graph, &testsink.sink.pin.IPin_iface);

    /* Connection with wildcards. */

    hr = IFilterGraph2_ConnectDirect(graph, source, &testsink.sink.pin.IPin_iface, NULL);
    ok(hr == VFW_E_NO_ACCEPTABLE_TYPES, "Got hr %#x.\n", hr);

    testsource.source_mt.bTemporalCompression = TRUE;
    hr = IFilterGraph2_ConnectDirect(graph, source, &testsink.sink.pin.IPin_iface, NULL);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(compare_media_types(&testsink.sink.pin.mt, &testsource.source_mt), "Media types didn't match.\n");
    ok(compare_media_types(&testsource.source.pin.mt, &testsink.sink.pin.mt), "Media types didn't match.\n");
    IFilterGraph2_Disconnect(graph, source);
    IFilterGraph2_Disconnect(graph, &testsink.sink.pin.IPin_iface);

    req_mt.majortype = GUID_NULL;
    req_mt.bTemporalCompression = FALSE;
    hr = IFilterGraph2_ConnectDirect(graph, source, &testsink.sink.pin.IPin_iface, &req_mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(compare_media_types(&testsink.sink.pin.mt, &testsource.source_mt), "Media types didn't match.\n");
    ok(compare_media_types(&testsource.source.pin.mt, &testsink.sink.pin.mt), "Media types didn't match.\n");
    IFilterGraph2_Disconnect(graph, source);
    IFilterGraph2_Disconnect(graph, &testsink.sink.pin.IPin_iface);

    req_mt.subtype = MEDIASUBTYPE_RGB32;
    hr = IFilterGraph2_ConnectDirect(graph, source, &testsink.sink.pin.IPin_iface, &req_mt);
    ok(hr == VFW_E_NO_ACCEPTABLE_TYPES, "Got hr %#x.\n", hr);

    req_mt.subtype = GUID_NULL;
    hr = IFilterGraph2_ConnectDirect(graph, source, &testsink.sink.pin.IPin_iface, &req_mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(compare_media_types(&testsink.sink.pin.mt, &testsource.source_mt), "Media types didn't match.\n");
    ok(compare_media_types(&testsource.source.pin.mt, &testsink.sink.pin.mt), "Media types didn't match.\n");
    IFilterGraph2_Disconnect(graph, source);
    IFilterGraph2_Disconnect(graph, &testsink.sink.pin.IPin_iface);

    req_mt.formattype = FORMAT_None;
    hr = IFilterGraph2_ConnectDirect(graph, source, &testsink.sink.pin.IPin_iface, &req_mt);
    ok(hr == VFW_E_NO_ACCEPTABLE_TYPES, "Got hr %#x.\n", hr);

    req_mt.majortype = MEDIATYPE_Video;
    req_mt.subtype = MEDIASUBTYPE_RGB8;
    req_mt.formattype = GUID_NULL;
    hr = IFilterGraph2_ConnectDirect(graph, source, &testsink.sink.pin.IPin_iface, &req_mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(compare_media_types(&testsink.sink.pin.mt, &testsource.source_mt), "Media types didn't match.\n");
    ok(compare_media_types(&testsource.source.pin.mt, &testsink.sink.pin.mt), "Media types didn't match.\n");
    IFilterGraph2_Disconnect(graph, source);
    IFilterGraph2_Disconnect(graph, &testsink.sink.pin.IPin_iface);

    req_mt.subtype = MEDIASUBTYPE_RGB32;
    hr = IFilterGraph2_ConnectDirect(graph, source, &testsink.sink.pin.IPin_iface, &req_mt);
    ok(hr == VFW_E_NO_ACCEPTABLE_TYPES, "Got hr %#x.\n", hr);

    req_mt.subtype = GUID_NULL;
    hr = IFilterGraph2_ConnectDirect(graph, source, &testsink.sink.pin.IPin_iface, &req_mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(compare_media_types(&testsink.sink.pin.mt, &testsource.source_mt), "Media types didn't match.\n");
    ok(compare_media_types(&testsource.source.pin.mt, &testsink.sink.pin.mt), "Media types didn't match.\n");
    IFilterGraph2_Disconnect(graph, source);
    IFilterGraph2_Disconnect(graph, &testsink.sink.pin.IPin_iface);

    req_mt.majortype = MEDIATYPE_Audio;
    hr = IFilterGraph2_ConnectDirect(graph, source, &testsink.sink.pin.IPin_iface, &req_mt);
    ok(hr == VFW_E_NO_ACCEPTABLE_TYPES, "Got hr %#x.\n", hr);

    testsource.source_mt.majortype = testsource.source_mt.subtype = testsource.source_mt.formattype = GUID_NULL;
    req_mt.majortype = req_mt.subtype = req_mt.formattype = GUID_NULL;
    hr = IFilterGraph2_ConnectDirect(graph, source, &testsink.sink.pin.IPin_iface, &req_mt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(compare_media_types(&testsink.sink.pin.mt, &testsource.source_mt), "Media types didn't match.\n");
    ok(compare_media_types(&testsource.source.pin.mt, &testsink.sink.pin.mt), "Media types didn't match.\n");
    IFilterGraph2_Disconnect(graph, source);
    IFilterGraph2_Disconnect(graph, &testsink.sink.pin.IPin_iface);

    req_mt.majortype = MEDIATYPE_Video;
    hr = IFilterGraph2_ConnectDirect(graph, source, &testsink.sink.pin.IPin_iface, &req_mt);
    ok(hr == VFW_E_NO_ACCEPTABLE_TYPES, "Got hr %#x.\n", hr);
    req_mt.majortype = GUID_NULL;

    req_mt.subtype = MEDIASUBTYPE_RGB8;
    hr = IFilterGraph2_ConnectDirect(graph, source, &testsink.sink.pin.IPin_iface, &req_mt);
    ok(hr == VFW_E_NO_ACCEPTABLE_TYPES, "Got hr %#x.\n", hr);
    req_mt.subtype = GUID_NULL;

    req_mt.formattype = FORMAT_None;
    hr = IFilterGraph2_ConnectDirect(graph, source, &testsink.sink.pin.IPin_iface, &req_mt);
    ok(hr == VFW_E_NO_ACCEPTABLE_TYPES, "Got hr %#x.\n", hr);
    req_mt.formattype = GUID_NULL;

    /* Test enumeration of sink media types. */

    testsink.sink_mt = &req_mt;
    req_mt.majortype = MEDIATYPE_Audio;
    hr = IFilterGraph2_ConnectDirect(graph, source, &testsink.sink.pin.IPin_iface, NULL);
    ok(hr == VFW_E_NO_ACCEPTABLE_TYPES, "Got hr %#x.\n", hr);
    req_mt.majortype = GUID_NULL;

    req_mt.bTemporalCompression = TRUE;
    req_mt.lSampleSize = 444;
    hr = IFilterGraph2_ConnectDirect(graph, source, &testsink.sink.pin.IPin_iface, NULL);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(compare_media_types(&testsink.sink.pin.mt, &req_mt), "Media types didn't match.\n");
    ok(compare_media_types(&testsource.source.pin.mt, &testsink.sink.pin.mt), "Media types didn't match.\n");

    hr = IPin_EnumMediaTypes(sink, &enummt);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IEnumMediaTypes_Next(enummt, 1, &pmt, NULL);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    ok(compare_media_types(pmt, testsink.sink_mt), "Media types didn't match.\n");
    IEnumMediaTypes_Release(enummt);

    IFilterGraph2_Disconnect(graph, source);
    IFilterGraph2_Disconnect(graph, &testsink.sink.pin.IPin_iface);

    hr = IFilterGraph2_Disconnect(graph, sink);
    ok(hr == S_OK, "Got hr %#x.\n", hr);
    hr = IFilterGraph2_Disconnect(graph, sink);
    ok(hr == S_FALSE, "Got hr %#x.\n", hr);
    ok(testsource.source.pin.peer == sink, "Got peer %p.\n", testsource.source.pin.peer);
    IFilterGraph2_Disconnect(graph, &testsource.source.pin.IPin_iface);

    peer = (IPin *)0xdeadbeef;
    hr = IPin_ConnectedTo(sink, &peer);
    ok(hr == VFW_E_NOT_CONNECTED, "Got hr %#x.\n", hr);
    ok(!peer, "Got peer %p.\n", peer);

    hr = IPin_ConnectionMediaType(sink, &mt);
    ok(hr == VFW_E_NOT_CONNECTED, "Got hr %#x.\n", hr);

    IMemInputPin_Release(input);
    IPin_Release(sink);
    IPin_Release(source);
    IMediaControl_Release(control);
    ref = IFilterGraph2_Release(graph);
    ok(!ref, "Got outstanding refcount %d.\n", ref);
    ISampleGrabber_Release(grabber);
    ref = IBaseFilter_Release(filter);
    ok(!ref, "Got outstanding refcount %d.\n", ref);
    ref = IBaseFilter_Release(&testsource.filter.IBaseFilter_iface);
    ok(!ref, "Got outstanding refcount %d.\n", ref);
    ref = IBaseFilter_Release(&testsink.filter.IBaseFilter_iface);
    ok(!ref, "Got outstanding refcount %d.\n", ref);
}

START_TEST(samplegrabber)
{
    IBaseFilter *filter;
    HRESULT hr;

    CoInitialize(NULL);

    if (FAILED(hr = CoCreateInstance(&CLSID_SampleGrabber, NULL, CLSCTX_INPROC_SERVER,
            &IID_IBaseFilter, (void **)&filter)))
    {
        /* qedit.dll does not exist on 2003. */
        win_skip("Failed to create sample grabber filter, hr %#x.\n", hr);
        return;
    }
    IBaseFilter_Release(filter);

    test_interfaces();
    test_enum_pins();
    test_find_pin();
    test_pin_info();
    test_aggregation();
    test_media_types();
    test_connect_pin();

    CoUninitialize();
}
