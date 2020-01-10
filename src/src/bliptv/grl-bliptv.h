/*
 * Copyright (C) 2011 Intel Corporation.
 *
 * Contact: Iago Toral Quiroga <itoral@igalia.com>
 *
 * Authors: Lionel Landwerlin <lionel.g.landwerlin@linux.intel.com>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public License
 * as published by the Free Software Foundation; version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA
 *
 */

#ifndef _GRL_BLIPTV_H
#define _GRL_BLIPTV_H

#include <glib-object.h>
#include <grilo.h>

G_BEGIN_DECLS

#define GRL_TYPE_BLIPTV_SOURCE grl_bliptv_source_get_type()

#define GRL_BLIPTV_SOURCE(obj)                                  \
  (G_TYPE_CHECK_INSTANCE_CAST ((obj),                           \
                               GRL_TYPE_BLIPTV_SOURCE,          \
                               GrlBliptvSource))

#define GRL_BLIPTV_SOURCE_CLASS(klass)                          \
  (G_TYPE_CHECK_CLASS_CAST ((klass),                            \
                            GRL_TYPE_BLIPTV_SOURCE,             \
                            GrlBliptvSourceClass))

#define GRL_IS_BLIPTV_SOURCE(obj)                       \
  (G_TYPE_CHECK_INSTANCE_TYPE ((obj),                   \
                               GRL_TYPE_BLIPTV_SOURCE))

#define GRL_IS_BLIPTV_SOURCE_CLASS(klass)              \
  (G_TYPE_CHECK_CLASS_TYPE ((klass),                   \
                            GRL_TYPE_BLIPTV_SOURCE))

#define GRL_BLIPTV_SOURCE_GET_CLASS(obj)                        \
  (G_TYPE_INSTANCE_GET_CLASS ((obj),                            \
                              GRL_TYPE_BLIPTV_SOURCE,           \
                              GrlBliptvSourceClass))

typedef struct _GrlBliptvSource        GrlBliptvSource;
typedef struct _GrlBliptvSourceClass   GrlBliptvSourceClass;
typedef struct _GrlBliptvSourcePrivate GrlBliptvSourcePrivate;

struct _GrlBliptvSource
{
  GrlSource parent;

  /*< private >*/
  GrlBliptvSourcePrivate *priv;
};

struct _GrlBliptvSourceClass
{
  GrlSourceClass parent_class;
};

GType grl_bliptv_source_get_type (void) G_GNUC_CONST;

G_END_DECLS

#endif /* _GRL_BLIPTV_H */
